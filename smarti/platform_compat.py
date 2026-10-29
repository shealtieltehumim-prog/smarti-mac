"""Cross-platform helpers that let Smarti run on Windows and macOS.

The original application targets Windows only. This module collects every
operating-system specific behaviour behind small, individually testable
functions so the rest of the code base only has to ask "what does this platform
do?" instead of calling Win32 APIs directly.

Nothing here imports Qt, so it is safe to import very early.
"""
from __future__ import annotations

import base64
import json
import logging
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

IS_WINDOWS = sys.platform == "win32"
IS_MACOS = sys.platform == "darwin"
IS_POSIX = os.name == "posix"

PLATFORM_LABEL = "macOS" if IS_MACOS else ("Windows" if IS_WINDOWS else "Linux")
SHELL_LABEL = "zsh" if IS_MACOS else ("PowerShell" if IS_WINDOWS else "bash")

# subprocess "creationflags" is only valid on Windows; passing a non-zero value
# on POSIX raises ValueError, so everything funnels through this constant.
CREATE_NO_WINDOW = 0x08000000 if IS_WINDOWS else 0

LOCAL_SECRET_TAG = "mac1:"
_LOCAL_KEY_SERVICE = "SmartiAI"
_LOCAL_KEY_NAME = "__smarti_local_data_key__"

_log = logging.getLogger(__name__)


# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
def macos_application_support(app_name="SmartiAI"):
    return os.path.join(os.path.expanduser("~"), "Library", "Application Support", app_name)


def macos_caches_dir(app_name="SmartiAI"):
    return os.path.join(os.path.expanduser("~"), "Library", "Caches", app_name)


def default_user_data_candidates(app_name="SmartiAI"):
    """Preferred per-user data directories in priority order."""
    if IS_MACOS:
        return [macos_application_support(app_name)]
    if IS_WINDOWS:
        return [
            os.path.join(base, app_name)
            for base in (os.environ.get("APPDATA"), os.environ.get("LOCALAPPDATA"))
            if base
        ]
    base = os.environ.get("XDG_DATA_HOME") or os.path.join(os.path.expanduser("~"), ".local", "share")
    return [os.path.join(base, app_name)]


def user_home():
    if IS_WINDOWS:
        return os.environ.get("USERPROFILE") or os.path.expanduser("~")
    return os.path.expanduser("~")


def documents_dir():
    candidate = os.path.join(user_home(), "Documents")
    return candidate if os.path.isdir(candidate) else ""


def temp_dir():
    return tempfile.gettempdir()


def browser_profile_root(fallback):
    """Directory that holds Smarti's private Chrome profile."""
    if IS_MACOS:
        return macos_application_support("SmartiAI")
    if IS_WINDOWS:
        return os.environ.get("LOCALAPPDATA", fallback)
    return fallback


def chrome_executable_candidates():
    if IS_MACOS:
        home = os.path.expanduser("~")
        return [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            os.path.join(home, "Applications", "Google Chrome.app", "Contents", "MacOS", "Google Chrome"),
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        ]
    return []


def macos_managed_tool_dirs():
    """Extra PATH entries that GUI-launched apps do not inherit on macOS."""
    home = os.path.expanduser("~")
    return [
        "/opt/homebrew/bin",
        "/opt/homebrew/sbin",
        "/usr/local/bin",
        "/usr/local/sbin",
        os.path.join(home, ".local", "bin"),
        os.path.join(home, ".cargo", "bin"),
    ]


# --------------------------------------------------------------------------
# osascript / defaults helpers
# --------------------------------------------------------------------------
def applescript_quote(value):
    """Return ``value`` as a safely quoted AppleScript string literal."""
    text = str(value if value is not None else "")
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    return '"' + text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", '" & linefeed & "') + '"'


def run_osascript(script, *, language=None, timeout=15, args=None):
    """Run AppleScript/JXA. Returns ``(returncode, stdout, stderr)``."""
    if not IS_MACOS:
        return 1, "", "osascript is only available on macOS"
    command = ["osascript"]
    if language:
        command += ["-l", str(language)]
    command += ["-e", str(script)]
    if args:
        command += [str(item) for item in args]
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        return completed.returncode, (completed.stdout or "").strip(), (completed.stderr or "").strip()
    except subprocess.TimeoutExpired:
        return 124, "", f"osascript timed out after {timeout}s"
    except Exception as exc:  # pragma: no cover - defensive
        return 1, "", str(exc)


def macos_is_dark_mode(default=True):
    if not IS_MACOS:
        return default
    try:
        completed = subprocess.run(
            ["defaults", "read", "-g", "AppleInterfaceStyle"],
            capture_output=True, text=True, timeout=3,
        )
        # In light mode the key does not exist and `defaults` exits non-zero.
        return completed.returncode == 0 and "dark" in (completed.stdout or "").lower()
    except Exception:
        return default


def macos_set_muted(muted):
    rc, _out, err = run_osascript(f"set volume output muted {'true' if muted else 'false'}", timeout=5)
    return rc == 0, err


def macos_display_notification(title, body, subtitle="", sound=False):
    parts = [f"display notification {applescript_quote(body)} with title {applescript_quote(title)}"]
    if subtitle:
        parts.append(f"subtitle {applescript_quote(subtitle)}")
    if sound:
        parts.append('sound name "Glass"')
    rc, _out, err = run_osascript(" ".join(parts), timeout=8)
    return rc == 0, err


def macos_set_clipboard(text):
    try:
        completed = subprocess.run(
            ["pbcopy"], input=str(text).encode("utf-8"), capture_output=True, timeout=10,
            env={**os.environ, "LC_ALL": "en_US.UTF-8"},
        )
        return completed.returncode == 0, (completed.stderr or b"").decode("utf-8", "replace").strip()
    except Exception as exc:
        return False, str(exc)


def macos_play_sound(path, *, wait=True):
    """Play an audio file with the built-in ``afplay`` utility."""
    if not IS_MACOS or not path or not os.path.exists(path):
        return False
    try:
        proc = subprocess.Popen(["afplay", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if wait:
            proc.wait(timeout=60)
        return True
    except Exception as exc:
        _log.warning("afplay failed for %s: %s", path, exc)
        return False


def macos_play_system_sound(kind="end"):
    name = {"start": "Pop", "end": "Tink", "timeout": "Basso"}.get(str(kind or ""), "Tink")
    return macos_play_sound(f"/System/Library/Sounds/{name}.aiff")


def macos_open(target, *, app=None, reveal=False):
    """Open a file, folder or URL like double-clicking it in Finder."""
    command = ["open"]
    if reveal:
        command.append("-R")
    if app:
        command += ["-a", str(app)]
    command.append(str(target))
    try:
        completed = subprocess.run(command, capture_output=True, text=True, timeout=15)
        if completed.returncode != 0:
            return False, (completed.stderr or completed.stdout or "").strip()
        return True, ""
    except Exception as exc:
        return False, str(exc)


def open_path_with_default_app(path):
    """Open a file/folder/URL with the OS default handler (``os.startfile`` replacement)."""
    if IS_WINDOWS:
        os.startfile(str(path))  # type: ignore[attr-defined]
        return
    if IS_MACOS:
        ok, err = macos_open(path)
        if not ok:
            raise OSError(err or "open failed")
        return
    opener = shutil.which("xdg-open")
    if not opener:
        raise OSError("No default opener is available on this system")
    subprocess.Popen([opener, str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# --------------------------------------------------------------------------
# Installed application discovery (macOS)
# --------------------------------------------------------------------------
def macos_app_search_roots():
    home = os.path.expanduser("~")
    return [
        "/Applications",
        "/Applications/Utilities",
        "/System/Applications",
        "/System/Applications/Utilities",
        "/System/Library/CoreServices",
        os.path.join(home, "Applications"),
    ]


def macos_list_installed_apps(roots=None, max_depth=2):
    """Return ``[{"name", "path", "bundle"}]`` for ``.app`` bundles."""
    apps = []
    seen = set()
    for root in (roots if roots is not None else macos_app_search_roots()):
        if not os.path.isdir(root):
            continue
        root = os.path.abspath(root)
        base_depth = root.rstrip(os.sep).count(os.sep)
        for current, dirs, _files in os.walk(root):
            depth = current.rstrip(os.sep).count(os.sep) - base_depth
            kept = []
            for name in sorted(dirs):
                full = os.path.join(current, name)
                if name.lower().endswith(".app"):
                    key = os.path.realpath(full)
                    if key not in seen:
                        seen.add(key)
                        apps.append({
                            "name": name[:-4],
                            "path": full,
                            "bundle": name,
                        })
                    continue  # do not descend into bundles
                if depth + 1 < max_depth:
                    kept.append(name)
            dirs[:] = kept
    return apps


# --------------------------------------------------------------------------
# Settings panes / system apps
# --------------------------------------------------------------------------
MACOS_SETTINGS_TARGETS = {
    "calendar": ("app", "Calendar"),
    "clock": ("app", "Clock"),
    "alarms": ("app", "Clock"),
    "notification_settings": ("url", "x-apple.systempreferences:com.apple.Notifications-Settings.extension"),
    "focus_settings": ("url", "x-apple.systempreferences:com.apple.Focus-Settings.extension"),
}


def macos_open_system_target(target):
    kind, value = MACOS_SETTINGS_TARGETS.get(str(target or "").strip().lower(), (None, None))
    if not kind:
        return False, f"unknown target: {target}"
    if kind == "app":
        return _open_app_by_name(value)
    return macos_open(value)


def _open_app_by_name(name):
    try:
        completed = subprocess.run(["open", "-a", str(name)], capture_output=True, text=True, timeout=15)
        if completed.returncode != 0:
            return False, (completed.stderr or completed.stdout or "").strip()
        return True, ""
    except Exception as exc:
        return False, str(exc)


# --------------------------------------------------------------------------
# Sleep prevention (Windows SetThreadExecutionState equivalent)
# --------------------------------------------------------------------------
_caffeinate_lock = threading.Lock()
_caffeinate_users = 0
_caffeinate_proc = None


def macos_prevent_sleep(enabled):
    """Reference-counted ``caffeinate -i``. Returns True while active."""
    global _caffeinate_users, _caffeinate_proc
    if not IS_MACOS:
        return False
    with _caffeinate_lock:
        if enabled:
            _caffeinate_users += 1
            if _caffeinate_proc is None or _caffeinate_proc.poll() is not None:
                try:
                    _caffeinate_proc = subprocess.Popen(
                        ["caffeinate", "-i", "-w", str(os.getpid())],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                    )
                except Exception as exc:
                    _caffeinate_users = max(0, _caffeinate_users - 1)
                    _log.warning("caffeinate failed: %s", exc)
                    return False
            return True
        _caffeinate_users = max(0, _caffeinate_users - 1)
        if _caffeinate_users == 0 and _caffeinate_proc is not None:
            try:
                _caffeinate_proc.terminate()
            except Exception:
                pass
            _caffeinate_proc = None
        return False


# --------------------------------------------------------------------------
# Process-tree termination for POSIX
# --------------------------------------------------------------------------
def posix_popen_kwargs():
    """Extra Popen kwargs so children get their own process group."""
    return {"start_new_session": True} if IS_POSIX else {}


def terminate_process_tree_posix(proc, grace=1.5):
    """SIGTERM then SIGKILL the whole process group of ``proc``."""
    if proc is None or proc.poll() is not None:
        return
    try:
        pgid = os.getpgid(proc.pid)
    except Exception:
        pgid = None
    try:
        if pgid and pgid != os.getpgid(0):
            os.killpg(pgid, signal.SIGTERM)
        else:
            proc.terminate()
    except Exception:
        pass
    deadline = time.time() + grace
    while time.time() < deadline:
        if proc.poll() is not None:
            return
        time.sleep(0.05)
    try:
        if pgid and pgid != os.getpgid(0):
            os.killpg(pgid, signal.SIGKILL)
        else:
            proc.kill()
    except Exception:
        try:
            proc.kill()
        except Exception:
            pass


# --------------------------------------------------------------------------
# Local secret protection (replacement for Windows DPAPI)
# --------------------------------------------------------------------------
_key_lock = threading.Lock()
_cached_key = None


def _local_key_file():
    return os.path.join(macos_application_support("SmartiAI") if IS_MACOS else os.path.join(os.path.expanduser("~"), ".smarti"), ".local_data_key")


def _read_keychain_key():
    """Return ``(key, reachable)``; ``reachable`` is False when the Keychain raised (locked/denied)."""
    try:
        import keyring
        return keyring.get_password(_LOCAL_KEY_SERVICE, _LOCAL_KEY_NAME), True
    except Exception as exc:
        _log.info("Keychain unavailable for local key: %s", exc)
        return None, False


def _read_file_key():
    path = _local_key_file()
    try:
        if os.path.exists(path):
            return Path(path).read_text(encoding="ascii").strip() or None
    except Exception:
        pass
    return None


def _load_or_create_local_key():
    """Fernet key stored in the macOS Keychain (file fallback, mode 0600).

    A new key is only generated when no existing key could be found; a Keychain that merely failed to
    answer (locked / access denied) never causes an existing key to be replaced.
    """
    global _cached_key
    with _key_lock:
        if _cached_key:
            return _cached_key
        key, keychain_reachable = _read_keychain_key()
        if not key:
            key = _read_file_key()
        if not key:
            from cryptography.fernet import Fernet
            key = Fernet.generate_key().decode("ascii")
            stored = False
            if keychain_reachable:
                try:
                    import keyring
                    keyring.set_password(_LOCAL_KEY_SERVICE, _LOCAL_KEY_NAME, key)
                    stored = keyring.get_password(_LOCAL_KEY_SERVICE, _LOCAL_KEY_NAME) == key
                except Exception as exc:
                    _log.info("Could not store local key in Keychain: %s", exc)
            if not stored:
                path = _local_key_file()
                os.makedirs(os.path.dirname(path), exist_ok=True)
                fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
                with os.fdopen(fd, "w", encoding="ascii") as handle:
                    handle.write(key)
        _cached_key = key.encode("ascii")
        return _cached_key


def _candidate_keys():
    keys = []
    for item in (_load_or_create_local_key(), (_read_keychain_key()[0] or "").encode("ascii"), (_read_file_key() or "").encode("ascii")):
        if item and item not in keys:
            keys.append(item)
    return keys


def protect_local_secret(text):
    """Encrypt ``text`` with the per-user key. Returns a token or ``None``."""
    try:
        from cryptography.fernet import Fernet
        token = Fernet(_load_or_create_local_key()).encrypt(str(text).encode("utf-8"))
        return LOCAL_SECRET_TAG + token.decode("ascii")
    except Exception as exc:
        _log.warning("Local secret protection failed: %s", exc)
        return None


def unprotect_local_secret(payload):
    """Inverse of :func:`protect_local_secret`. Returns ``""`` on failure."""
    try:
        if not isinstance(payload, str) or not payload.startswith(LOCAL_SECRET_TAG):
            return ""
        from cryptography.fernet import Fernet
        token = payload[len(LOCAL_SECRET_TAG):].encode("ascii")
        for key in _candidate_keys():
            try:
                return Fernet(key).decrypt(token).decode("utf-8", "replace")
            except Exception:
                continue
        return ""
    except Exception:
        return ""


def _reset_local_key_cache_for_tests():
    global _cached_key
    with _key_lock:
        _cached_key = None


# --------------------------------------------------------------------------
# Text localisation for prompts / tool descriptions
# --------------------------------------------------------------------------
# Tool identifiers (open_windows_app, windows_search, ...) stay unchanged because
# they are part of the persisted settings and the tool protocol. Only the
# human/model-facing wording is adapted.


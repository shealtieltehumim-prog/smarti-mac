#!/usr/bin/env bash
# Build "Smarti AI Agent.app" and a DMG on macOS (Apple Silicon or Intel).
# Usage: scripts/build_macos.sh [--skip-runtime]
# Requirements: macOS 11+, Homebrew (brew install portaudio), Python 3.12 (uv will fetch it), curl.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
BUILD="$ROOT/build"
DIST="$ROOT/dist"
CACHE="$ROOT/.build-cache"
APP_NAME="Smarti AI Agent"
APP="$DIST/$APP_NAME.app"
VERSION="$(python3 - <<'PY'
import re
src = open("smarti/common.py", encoding="utf-8").read()
m = re.search(r'APP_VERSION\s*=\s*["\']([^"\']+)', src)
print((m.group(1) if m else "0.87.0").lstrip("vV"))
PY
)"
ARCH="$(uname -m)"
SKIP_RUNTIME=0
[[ "${1:-}" == "--skip-runtime" ]] && SKIP_RUNTIME=1

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "This script must run on macOS." >&2
  exit 1
fi

if ! command -v uv >/dev/null 2>&1; then
  echo "Installing uv..."
  python3 -m pip install --user uv
  export PATH="$(python3 -c 'import site;print(site.USER_BASE)')/bin:$HOME/.local/bin:$PATH"
fi
command -v uv >/dev/null 2>&1 || { echo "uv not found; install it with: brew install uv" >&2; exit 1; }

# PyAudio builds from source on macOS and needs the Homebrew PortAudio headers.
if command -v brew >/dev/null 2>&1 && brew --prefix portaudio >/dev/null 2>&1; then
  export CFLAGS="-I$(brew --prefix portaudio)/include ${CFLAGS:-}"
  export LDFLAGS="-L$(brew --prefix portaudio)/lib ${LDFLAGS:-}"
fi

mkdir -p "$CACHE" "$BUILD" "$DIST"

echo "==> Creating build environment"
uv venv --python 3.12 "$BUILD/venv"
# shellcheck disable=SC1091
source "$BUILD/venv/bin/activate"
uv pip install -r requirements-macos.txt -r requirements-build.txt

echo "==> Running PyInstaller"
rm -rf "$BUILD/pyi" "$APP"
pyinstaller --noconfirm --clean --distpath "$DIST" --workpath "$BUILD/pyi" packaging/smarti-macos.spec

if [[ $SKIP_RUNTIME -eq 0 ]]; then
  echo "==> Preparing embedded runtime (Python + Node)"
  RUNTIME="$APP/Contents/Resources/runtime"
  rm -rf "$RUNTIME"; mkdir -p "$RUNTIME"

  # Python (python-build-standalone via uv), copied so the .app is self-contained.
  uv python install 3.12
  # Use the interpreter's real prefix (not the build venv that is currently activated).
  BASE_PY="$(uv python find --no-project --python-preference only-managed 3.12 2>/dev/null || uv python find 3.12)"
  PYHOME="$("$BASE_PY" -c 'import sys; print(sys.base_prefix)')"
  cp -R "$PYHOME" "$RUNTIME/python"
  # uv-managed interpreters are marked externally managed, which would block pip installs (build and runtime).
  find "$RUNTIME/python" -name EXTERNALLY-MANAGED -delete
  "$RUNTIME/python/bin/python3" -m ensurepip --upgrade >/dev/null 2>&1 || true
  "$RUNTIME/python/bin/python3" -m pip install --no-cache-dir --upgrade pip
  "$RUNTIME/python/bin/python3" -m pip install --no-cache-dir -r requirements-macos-runtime.txt

  # Node.js with pinned SHA256 checksums.
  case "$ARCH" in
    arm64)  NODE_KEY="arm64" ;;
    x86_64) NODE_KEY="x64" ;;
    *) echo "Unsupported architecture $ARCH" >&2; exit 1 ;;
  esac
  NODE_URL="$(python3 -c "import json;print(json.load(open('packaging/runtime-versions-macos.json'))['node']['$NODE_KEY']['url'])")"
  NODE_SHA="$(python3 -c "import json;print(json.load(open('packaging/runtime-versions-macos.json'))['node']['$NODE_KEY']['sha256'])")"
  NODE_TGZ="$CACHE/$(basename "$NODE_URL")"
  [[ -f "$NODE_TGZ" ]] || curl -fsSL "$NODE_URL" -o "$NODE_TGZ"
  echo "$NODE_SHA  $NODE_TGZ" | shasum -a 256 -c -
  mkdir -p "$RUNTIME/node-tmp"
  tar -xzf "$NODE_TGZ" -C "$RUNTIME/node-tmp"
  mv "$RUNTIME"/node-tmp/node-v* "$RUNTIME/node"
  rmdir "$RUNTIME/node-tmp"
fi

echo "==> Ad-hoc code signing"
if [[ -d "$APP/Contents/Resources/runtime" ]]; then
  # Sign embedded Mach-O binaries (python, node, *.so, *.dylib) individually first.
  find "$APP/Contents/Resources/runtime" -type f \( -name "*.so" -o -name "*.dylib" -o -perm -111 \) -print0 \
    | while IFS= read -r -d '' f; do
        if file "$f" | grep -q "Mach-O"; then codesign --force --sign - "$f" >/dev/null 2>&1 || true; fi
      done
fi
codesign --force --deep --sign - "$APP"
codesign --verify --deep --strict "$APP" && echo "signature ok"

echo "==> Creating DMG"
DMG="$DIST/SmartiAI-Agent-for-macOS-$VERSION-$ARCH.dmg"
STAGE="$BUILD/dmg"
rm -rf "$STAGE" "$DMG"; mkdir -p "$STAGE"
cp -R "$APP" "$STAGE/"
ln -s /Applications "$STAGE/Applications"
cp LICENSE NOTICE.md README_MAC.md "$STAGE/" 2>/dev/null || true
hdiutil create -volname "$APP_NAME" -srcfolder "$STAGE" -ov -format UDZO "$DMG"
echo
echo "Done: $DMG"
echo "First launch: right-click the app -> Open (the app is not notarized), or run:  xattr -cr \"/Applications/$APP_NAME.app\""

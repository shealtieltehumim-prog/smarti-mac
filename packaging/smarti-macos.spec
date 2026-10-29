# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for the macOS .app bundle (Smarti AI Agent for macOS)."""
from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_submodules


spec_path = Path(globals().get("__file__", Path(SPECPATH) / "smarti-macos.spec")).resolve()
repo_root = spec_path.parent.parent
app_icon = repo_root / "assets" / "smarti.icns"

datas = [
    (str(repo_root / "assets"), "assets"),
    (str(repo_root / "sitecustomize.py"), "."),
    (str(repo_root / "LICENSE"), "."),
    (str(repo_root / "NOTICE.md"), "."),
]

for package in ("certifi", "keyring", "truststore"):
    try:
        datas += collect_data_files(package)
    except Exception:
        pass

hiddenimports = [
    "PyQt6.QtWebEngineCore",
    "PyQt6.QtWebEngineWidgets",
    "keyring.backends.macOS",
]
for package in (
    "bs4",
    "docx",
    "edge_tts",
    "gtts",
    "keyring",
    "litellm",
    "markdown",
    "PIL",
    "fitz",
    "pymupdf",
    "pyaudio",
    "PyPDF2",
    "pyautogui",
    "pygame",
    "pytesseract",
    "send2trash",
    "speech_recognition",
    "truststore",
    "cryptography",
):
    try:
        hiddenimports += collect_submodules(package)
    except Exception:
        pass


a = Analysis(
    [str(repo_root / "smarti_core.pyw")],
    pathex=[str(repo_root)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["uiautomation", "windows_toasts", "win32com", "winrt", "keyboard"],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SmartiAI",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,          # native architecture of the build machine
    codesign_identity=None,    # ad-hoc signing is applied by scripts/build_macos.sh
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name="SmartiAI",
)

app = BUNDLE(
    coll,
    name="Smarti AI Agent.app",
    icon=str(app_icon),
    bundle_identifier="il.smarti.agent.macos",
    version="0.87.0",
    info_plist={
        "CFBundleName": "Smarti AI Agent",
        "CFBundleDisplayName": "Smarti AI Agent",
        "CFBundleShortVersionString": "0.87.0",
        "LSMinimumSystemVersion": "13.0",
        "NSHighResolutionCapable": True,
        "LSApplicationCategoryType": "public.app-category.productivity",
        "NSMicrophoneUsageDescription": "Smarti uses the microphone for voice input when you enable it.",
        "NSAppleEventsUsageDescription": "Smarti controls other apps (System Events) only when you enable computer control.",
        "NSDesktopFolderUsageDescription": "Smarti accesses files you ask it to work with.",
        "NSDocumentsFolderUsageDescription": "Smarti accesses files you ask it to work with.",
        "NSDownloadsFolderUsageDescription": "Smarti accesses files you ask it to work with.",
        "CFBundleDevelopmentRegion": "he",
        "CFBundleLocalizations": ["he", "en"],
    },
)

"""Theme tokens, stylesheet snippets, and generated UI assets."""
from .common import *

# ==========================================
# Smarti premium UI design system
# ==========================================

THEME_OPTIONS = ("system", "dark", "light")
DEFAULT_THEME_MODE = "dark"
APP_FONT_FAMILY = "Heebo"
MONO_FONT_CSS = "'SF Mono', Menlo, Monaco, Consolas, 'Courier New', monospace"
DISPLAY_FONT_FAMILY = "Frank Ruhl Libre"   # ceremonial Hebrew (siddur-style) face used for the About credit
FALLBACK_FONT_CSS = "'.AppleSystemUIFont', 'Helvetica Neue', 'Noto Sans Hebrew', Arial, sans-serif"
APP_FONT_SOURCE_PATH = ""
_APP_FONT_CACHE_PATH = None
_APP_FONT_CACHE_FAMILY = None
TOOLTIP_BG_COLOR = "#303134"
TOOLTIP_TEXT_COLOR = "#FFFFFF"
CLOSE_SVG_PATH = ""

# Google / Material 3 inspired palette: tonal surfaces, a single blue accent, soft translucent glass.
BRAND_ACCENT_COLOR = "#4285F4"      # Google blue
BRAND_SECONDARY_COLOR = "#34A853"   # Google green
BRAND_PINK_COLOR = "#EA4335"        # Google red (kept for legacy token names)
BRAND_VIOLET_COLOR = "#9334E6"
BRAND_WARM_COLOR = "#FBBC04"        # Google yellow
DANGER_COLOR = "#E5493A"

THEME_PALETTES = {
    "dark": {
        "BG_COLOR": "#131314",
        "BG_ELEVATED_COLOR": "#1B1C1E",
        "PANEL_COLOR": "#1E1F20",
        "PANEL_ELEVATED_COLOR": "#282A2C",
        "FIELD_COLOR": "#232527",
        "FIELD_HOVER_COLOR": "#2D2F32",
        "TEXT_COLOR": "#E8EAED",
        "MUTED_TEXT_COLOR": "#C4C7C5",
        "SUBTLE_TEXT_COLOR": "#9AA0A6",
        "ACCENT_COLOR": "#A8C7FA",
        "ACCENT_HOVER_COLOR": "#C2D7FB",
        "WARNING_COLOR": "#FDD663",
        "ACCENT_SECONDARY_COLOR": "#81C995",
        "ACCENT_PINK_COLOR": "#A8C7FA",
        "ACCENT_WARM_COLOR": "#A8C7FA",
        "ACCENT_TEXT_COLOR": "#062E6F",
        "LINE_COLOR": "rgba(168,199,250,0.45)",
        "SOFT_LINE_COLOR": "rgba(232,234,237,0.10)",
        "GLASS_COLOR": "rgba(40,42,44,0.62)",
        "GLASS_STRONG_COLOR": "rgba(40,42,44,0.86)",
        "MESH_A": "#131314",
        "MESH_B": "#151922",
        "MESH_C": "#171A26",
        "MESH_D": "#181520",
        "USER_BUBBLE_COLOR": "#0B57D0",
        "USER_BUBBLE_BORDER": "rgba(168,199,250,0.30)",
        "INPUT_GRADIENT_END": "#2B2D30",
        "CARD_GRADIENT_END": "#202224",
        "TOP_GRADIENT_A": "#17181A",
        "TOP_GRADIENT_B": "#17181A",
        "TOP_GRADIENT_C": "#17181A",
        "MENU_BG_COLOR": "#2B2D30",
        "TOOLTIP_BG_COLOR": "#E8EAED",
        "TOOLTIP_TEXT_COLOR": "#202124",
        "BUBBLE_AGENT_END": "#232527",
        "BUBBLE_USER_TEXT": "#FFFFFF",
        "CODE_BG_COLOR": "rgba(0,0,0,0.38)",
        "HOVER_TINT": "rgba(232,234,237,0.08)",
        "ACCENT_TINT": "rgba(168,199,250,0.14)",
        "ACCENT_TINT_STRONG": "rgba(168,199,250,0.26)",
        "FIELD_TEXT_COLOR": "#F1F3F4",
    },
    "light": {
        "BG_COLOR": "#F8FAFD",
        "BG_ELEVATED_COLOR": "#FFFFFF",
        "PANEL_COLOR": "#F0F4F9",
        "PANEL_ELEVATED_COLOR": "#E9EEF6",
        "FIELD_COLOR": "#EEF2F8",
        "FIELD_HOVER_COLOR": "#E4EAF4",
        "TEXT_COLOR": "#1F1F1F",
        "MUTED_TEXT_COLOR": "#444746",
        "SUBTLE_TEXT_COLOR": "#747775",
        "ACCENT_COLOR": "#0B57D0",
        "ACCENT_HOVER_COLOR": "#0A4DB8",
        "WARNING_COLOR": "#B06000",
        "ACCENT_SECONDARY_COLOR": "#146C2E",
        "ACCENT_PINK_COLOR": "#0B57D0",
        "ACCENT_WARM_COLOR": "#0B57D0",
        "ACCENT_TEXT_COLOR": "#FFFFFF",
        "LINE_COLOR": "rgba(11,87,208,0.42)",
        "SOFT_LINE_COLOR": "rgba(31,31,31,0.10)",
        "GLASS_COLOR": "rgba(255,255,255,0.70)",
        "GLASS_STRONG_COLOR": "rgba(255,255,255,0.92)",
        "MESH_A": "#F8FAFD",
        "MESH_B": "#EEF4FC",
        "MESH_C": "#F1F0FA",
        "MESH_D": "#F6F1F7",
        "USER_BUBBLE_COLOR": "#D3E3FD",
        "USER_BUBBLE_BORDER": "rgba(11,87,208,0.16)",
        "INPUT_GRADIENT_END": "#F0F4F9",
        "CARD_GRADIENT_END": "#F6F9FD",
        "TOP_GRADIENT_A": "#FFFFFF",
        "TOP_GRADIENT_B": "#FFFFFF",
        "TOP_GRADIENT_C": "#FFFFFF",
        "MENU_BG_COLOR": "#FFFFFF",
        "TOOLTIP_BG_COLOR": "#303134",
        "TOOLTIP_TEXT_COLOR": "#FFFFFF",
        "BUBBLE_AGENT_END": "#F4F7FB",
        "BUBBLE_USER_TEXT": "#041E49",
        "CODE_BG_COLOR": "rgba(31,31,31,0.06)",
        "HOVER_TINT": "rgba(31,31,31,0.06)",
        "ACCENT_TINT": "rgba(11,87,208,0.09)",
        "ACCENT_TINT_STRONG": "rgba(11,87,208,0.17)",
        "FIELD_TEXT_COLOR": "#1F1F1F",
    },
}

THEME_EXPORT_NAMES = (
    "CURRENT_THEME_MODE", "CURRENT_THEME",
    "BG_COLOR", "BG_ELEVATED_COLOR", "PANEL_COLOR", "PANEL_ELEVATED_COLOR",
    "FIELD_COLOR", "FIELD_HOVER_COLOR", "TEXT_COLOR", "MUTED_TEXT_COLOR",
    "SUBTLE_TEXT_COLOR", "ACCENT_COLOR", "ACCENT_HOVER_COLOR", "WARNING_COLOR", "ACCENT_SECONDARY_COLOR",
    "ACCENT_PINK_COLOR", "ACCENT_WARM_COLOR", "ACCENT_TEXT_COLOR", "LINE_COLOR", "SOFT_LINE_COLOR",
    "INPUT_GRADIENT_END", "CARD_GRADIENT_END", "TOP_GRADIENT_A",
    "TOP_GRADIENT_B", "TOP_GRADIENT_C", "MENU_BG_COLOR", "TOOLTIP_BG_COLOR", "TOOLTIP_TEXT_COLOR", "BUBBLE_AGENT_END",
    "GLASS_COLOR", "GLASS_STRONG_COLOR", "MESH_A", "MESH_B", "MESH_C",
    "MESH_D", "USER_BUBBLE_COLOR", "USER_BUBBLE_BORDER",
    "BUBBLE_USER_TEXT", "CODE_BG_COLOR", "HOVER_TINT", "ACCENT_TINT",
    "ACCENT_TINT_STRONG", "FIELD_TEXT_COLOR", "CHECKMARK_SVG_PATH",
    "DROPDOWN_SVG_PATH", "RESET_SVG_PATH", "CHECKBOX_CSS", "COMBOBOX_CSS",
    "LINE_EDIT_CSS", "TEXT_EDIT_CSS", "PRIMARY_BUTTON_CSS",
    "SECONDARY_BUTTON_CSS", "DANGER_BUTTON_CSS", "NAV_CARD_CSS",
    "INPUT_FRAME_CSS", "SCROLLBAR_CSS", "SLIDER_CSS", "LOG_TEXT_CSS", "CLOSE_SVG_PATH",
)


def _normalize_theme_mode(mode):
    mode = str(mode or DEFAULT_THEME_MODE).strip().lower()
    return mode if mode in THEME_OPTIONS else DEFAULT_THEME_MODE


def _read_theme_mode_from_disk():
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            prefs = data.get("ui_preferences", {}) if isinstance(data, dict) else {}
            return _normalize_theme_mode(prefs.get("theme_mode", DEFAULT_THEME_MODE))
    except Exception:
        pass
    return DEFAULT_THEME_MODE


def _system_prefers_dark():
    if IS_MACOS:
        return macos_is_dark_mode(default=True)
    if os.name != "nt":
        return True
    try:
        import winreg
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return int(value) == 0
    except Exception:
        return True


def resolve_theme_mode(mode=None, settings=None):
    if mode is None and isinstance(settings, dict):
        mode = settings.get("ui_preferences", {}).get("theme_mode", DEFAULT_THEME_MODE)
    if mode is None:
        mode = _read_theme_mode_from_disk()
    mode = _normalize_theme_mode(mode)
    if mode == "system":
        return "dark" if _system_prefers_dark() else "light"
    return mode


def _svg_asset(filename, svg_text):
    path = ensure_ui_svg_asset(filename, svg_text)
    return path.replace("\\", "/") if path else ""


def themed_asset_candidates(*names):
    candidates = []
    alternate_theme = "light" if CURRENT_THEME == "dark" else "dark"
    for name in names:
        raw = str(name or "").strip()
        if not raw:
            continue
        if os.path.isabs(raw) or os.path.dirname(raw):
            candidates.append(raw)
            continue
        stem, ext = os.path.splitext(raw)
        if ext:
            candidates.append(f"{stem}_{CURRENT_THEME}{ext}")
            candidates.append(f"{stem}_{CURRENT_THEME} {ext}")
            candidates.append(raw)
            candidates.append(f"{stem} {ext}")
            candidates.append(f"{stem}_{alternate_theme}{ext}")
            candidates.append(f"{stem}_{alternate_theme} {ext}")
        else:
            for suffix in (".png", ".svg"):
                candidates.append(f"{raw}_{CURRENT_THEME}{suffix}")
                candidates.append(f"{raw}_{CURRENT_THEME} {suffix}")
            for suffix in (".png", ".svg"):
                candidates.append(f"{raw}{suffix}")
                candidates.append(f"{raw} {suffix}")
            for suffix in (".png", ".svg"):
                candidates.append(f"{raw}_{alternate_theme}{suffix}")
                candidates.append(f"{raw}_{alternate_theme} {suffix}")
    return list(dict.fromkeys(candidates))


def themed_asset_path(*names):
    for filename in themed_asset_candidates(*names):
        path = filename if os.path.isabs(filename) or os.path.dirname(filename) else os.path.join(ASSETS_DIR, filename)
        if os.path.exists(path):
            return path.replace("\\", "/")
    return ""


_BUNDLED_FONT_FILES = (
    "Heebo-Regular.ttf", "Heebo-Medium.ttf", "Heebo-Bold.ttf",
    "FrankRuhlLibre-Medium.ttf", "FrankRuhlLibre-Bold.ttf",
    "NotoSansHebrew-VariableFont_wdth,wght.ttf",
)


def _app_font_asset_path():
    for name in ("smarti_font.ttf", "smarti_font.otf", "Heebo-Regular.ttf"):
        path = os.path.join(ASSETS_DIR, name)
        if os.path.exists(path):
            return path
    try:
        for pattern in ("*.ttf", "*.otf"):
            matches = sorted(glob.glob(os.path.join(ASSETS_DIR, pattern)))
            if matches:
                return matches[0]
    except Exception:
        pass
    return ""


def _load_bundled_fonts():
    """Register every bundled font file once (Heebo UI face, Frank Ruhl display face, Noto fallback)."""
    loaded = {}
    for name in _BUNDLED_FONT_FILES:
        path = os.path.join(ASSETS_DIR, name)
        if not os.path.exists(path):
            continue
        try:
            font_id = QFontDatabase.addApplicationFont(path)
            if font_id >= 0:
                loaded[name] = list(QFontDatabase.applicationFontFamilies(font_id))
        except Exception as exc:
            logging.warning(f"Failed to load bundled font {name}: {exc}")
    return loaded


def resolve_app_font_family(default="Heebo"):
    global APP_FONT_FAMILY, APP_FONT_SOURCE_PATH, _APP_FONT_CACHE_PATH, _APP_FONT_CACHE_FAMILY, DISPLAY_FONT_FAMILY
    path = _app_font_asset_path()
    if not path:
        APP_FONT_FAMILY = default
        APP_FONT_SOURCE_PATH = ""
        _APP_FONT_CACHE_PATH = ""
        _APP_FONT_CACHE_FAMILY = default
        return APP_FONT_FAMILY
    if QApplication.instance() is None:
        APP_FONT_FAMILY = default
        APP_FONT_SOURCE_PATH = path
        return APP_FONT_FAMILY
    if _APP_FONT_CACHE_PATH == path and _APP_FONT_CACHE_FAMILY:
        APP_FONT_FAMILY = _APP_FONT_CACHE_FAMILY
        APP_FONT_SOURCE_PATH = path
        return APP_FONT_FAMILY
    family = default
    try:
        loaded = _load_bundled_fonts()
        main_name = os.path.basename(path)
        families = loaded.get(main_name)
        if not families:
            font_id = QFontDatabase.addApplicationFont(path)
            families = QFontDatabase.applicationFontFamilies(font_id) if font_id >= 0 else []
        family = str(families[0]).strip() if families else default
        display = loaded.get("FrankRuhlLibre-Bold.ttf") or loaded.get("FrankRuhlLibre-Medium.ttf")
        if display:
            DISPLAY_FONT_FAMILY = str(display[0]).strip() or DISPLAY_FONT_FAMILY
    except Exception as exc:
        logging.warning(f"Failed to load Smarti UI font asset {path}: {exc}")
        family = default
    _APP_FONT_CACHE_PATH = path
    _APP_FONT_CACHE_FAMILY = family
    APP_FONT_FAMILY = family
    APP_FONT_SOURCE_PATH = path
    return APP_FONT_FAMILY


def ui_font_family_css():
    family = resolve_app_font_family()
    safe_family = str(family or "Heebo").replace("\\", "\\\\").replace("'", "\\'")
    return f"'{safe_family}', {FALLBACK_FONT_CSS}"


def credit_font_family():
    """Ceremonial Hebrew face for the About credit.

    Drop a font file named ``kiddush_levana.ttf`` (or ``.otf``) into the assets folder to override the
    bundled Frank Ruhl Libre siddur-style face.
    """
    resolve_app_font_family()
    for name in ("kiddush_levana.ttf", "kiddush_levana.otf"):
        path = os.path.join(ASSETS_DIR, name)
        if os.path.exists(path) and QApplication.instance() is not None:
            try:
                font_id = QFontDatabase.addApplicationFont(path)
                families = QFontDatabase.applicationFontFamilies(font_id) if font_id >= 0 else []
                if families:
                    return str(families[0]).strip()
            except Exception:
                pass
    return DISPLAY_FONT_FAMILY


def ui_popup_font_family_css():
    return ui_font_family_css()


def app_font(point_size=10, weight=None):
    font = QFont(resolve_app_font_family(), int(point_size))
    if weight is not None:
        font.setWeight(weight)
    if app_uses_asset_font():
        font.setItalic(False)
    return font


def small_control_font(point_size=10, weight=QFont.Weight.Normal):
    """Use the configured asset font without heavy grid fitting at small sizes."""
    font = QFont(resolve_app_font_family(), int(point_size))
    if weight is not None:
        font.setWeight(weight)
    font.setHintingPreference(QFont.HintingPreference.PreferNoHinting)
    font.setStyleStrategy(QFont.StyleStrategy.PreferAntialias)
    if app_uses_asset_font():
        font.setItalic(False)
    return font


def app_uses_asset_font():
    resolve_app_font_family()
    return bool(APP_FONT_SOURCE_PATH)


def asset_font_normal_italic_widget_css():
    return "font-style: normal;" if app_uses_asset_font() else ""


def asset_font_normal_italic_html_css():
    return "i, em { font-style: normal; }" if app_uses_asset_font() else ""


def themed_icon(*names):
    for filename in themed_asset_candidates(*names):
        path = filename if os.path.isabs(filename) or os.path.dirname(filename) else os.path.join(ASSETS_DIR, filename)
        if os.path.exists(path):
            icon = QIcon(path)
            if not icon.isNull():
                return icon
    return QIcon()


def qcolor_from_css(value, fallback="#000000", alpha=None):
    text = str(value or "").strip()
    match = re.fullmatch(r"rgba?\(\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)(?:\s*,\s*([0-9.]+))?\s*\)", text)
    if match:
        r, g, b = [max(0, min(255, int(float(part)))) for part in match.group(1, 2, 3)]
        raw_alpha = match.group(4)
        if raw_alpha is None:
            a = 255
        else:
            parsed = float(raw_alpha)
            a = int(max(0.0, min(1.0, parsed)) * 255) if parsed <= 1 else max(0, min(255, int(parsed)))
        color = QColor(r, g, b, a)
    else:
        color = QColor(text)
        if not color.isValid():
            color = QColor(fallback)
    if alpha is not None:
        color.setAlpha(max(0, min(255, int(alpha))))
    return color


def set_themed_button_icon(button, names, fallback_text="", icon_size=20, clear_text=True):
    if isinstance(names, str):
        names = (names,)
    names = tuple(str(name) for name in (names or ()) if str(name or "").strip())
    button.setProperty("smartiIconNames", names)
    button.setProperty("smartiIconFallbackText", fallback_text)
    button.setProperty("smartiIconSize", int(icon_size))
    button.setProperty("smartiIconClearText", bool(clear_text))
    refresh_themed_button_icon(button)


def refresh_themed_button_icon(button):
    names = button.property("smartiIconNames")
    if not names:
        return
    fallback_text = button.property("smartiIconFallbackText")
    icon_size = int(button.property("smartiIconSize") or 20)
    clear_text = bool(button.property("smartiIconClearText"))
    icon = themed_icon(*tuple(names))
    if not icon.isNull():
        button.setIcon(icon)
        button.setIconSize(QSize(icon_size, icon_size))
        if clear_text:
            button.setText("")
    else:
        button.setIcon(QIcon())
        if fallback_text is not None:
            button.setText(str(fallback_text))


def set_themed_label_icon(label, names, fallback_text="", icon_size=28):
    if isinstance(names, str):
        names = (names,)
    names = tuple(str(name) for name in (names or ()) if str(name or "").strip())
    label.setProperty("smartiIconNames", names)
    label.setProperty("smartiIconFallbackText", fallback_text)
    label.setProperty("smartiIconSize", int(icon_size))
    refresh_themed_label_icon(label)


def refresh_themed_label_icon(label):
    names = label.property("smartiIconNames")
    if not names:
        return
    fallback_text = label.property("smartiIconFallbackText")
    icon_size = int(label.property("smartiIconSize") or 28)
    icon = themed_icon(*tuple(names))
    if not icon.isNull():
        label.setPixmap(icon.pixmap(icon_size, icon_size))
        label.setText("")
    else:
        label.setPixmap(QPixmap())
        if fallback_text is not None:
            label.setText(str(fallback_text))


def refresh_themed_widget_icons(root):
    widgets = [root] if root is not None else []
    try:
        widgets += root.findChildren(QWidget) if root is not None else []
    except Exception:
        pass
    for widget in widgets:
        if isinstance(widget, QPushButton):
            refresh_themed_button_icon(widget)
        elif isinstance(widget, QLabel):
            refresh_themed_label_icon(widget)


def _refresh_theme_exports(mode=None, settings=None):
    global CURRENT_THEME_MODE, CURRENT_THEME
    global APP_FONT_FAMILY, APP_FONT_SOURCE_PATH
    global BG_COLOR, BG_ELEVATED_COLOR, PANEL_COLOR, PANEL_ELEVATED_COLOR
    global FIELD_COLOR, FIELD_HOVER_COLOR, TEXT_COLOR, MUTED_TEXT_COLOR
    global SUBTLE_TEXT_COLOR, ACCENT_COLOR, ACCENT_HOVER_COLOR, WARNING_COLOR, ACCENT_SECONDARY_COLOR
    global ACCENT_PINK_COLOR, ACCENT_WARM_COLOR, ACCENT_TEXT_COLOR, LINE_COLOR, SOFT_LINE_COLOR
    global INPUT_GRADIENT_END, CARD_GRADIENT_END, TOP_GRADIENT_A
    global TOP_GRADIENT_B, TOP_GRADIENT_C, MENU_BG_COLOR, TOOLTIP_BG_COLOR, TOOLTIP_TEXT_COLOR, BUBBLE_AGENT_END
    global GLASS_COLOR, GLASS_STRONG_COLOR, MESH_A, MESH_B, MESH_C, MESH_D
    global USER_BUBBLE_COLOR, USER_BUBBLE_BORDER
    global BUBBLE_USER_TEXT, CODE_BG_COLOR, HOVER_TINT, ACCENT_TINT
    global ACCENT_TINT_STRONG, FIELD_TEXT_COLOR
    global CHECKMARK_SVG_PATH, DROPDOWN_SVG_PATH, RESET_SVG_PATH, CLOSE_SVG_PATH
    global CHECKBOX_CSS, COMBOBOX_CSS, LINE_EDIT_CSS, TEXT_EDIT_CSS
    global PRIMARY_BUTTON_CSS, SECONDARY_BUTTON_CSS, DANGER_BUTTON_CSS
    global NAV_CARD_CSS, INPUT_FRAME_CSS, SCROLLBAR_CSS, SLIDER_CSS, LOG_TEXT_CSS

    requested = mode
    if requested is None and isinstance(settings, dict):
        requested = settings.get("ui_preferences", {}).get("theme_mode", DEFAULT_THEME_MODE)
    if requested is None:
        requested = _read_theme_mode_from_disk()

    CURRENT_THEME_MODE = _normalize_theme_mode(requested)
    CURRENT_THEME = resolve_theme_mode(CURRENT_THEME_MODE, settings)
    palette = THEME_PALETTES[CURRENT_THEME]
    globals().update(palette)
    APP_FONT_FAMILY = resolve_app_font_family()

    CHECKMARK_SVG_PATH = _svg_asset(
        f"checkmark_{CURRENT_THEME}.svg",
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{ACCENT_TEXT_COLOR}" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L19 7"/></svg>'
    )
    DROPDOWN_SVG_PATH = _svg_asset(
        f"dropdown_{CURRENT_THEME}.svg",
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{ACCENT_COLOR}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>'
    )
    RESET_SVG_PATH = _svg_asset(
        f"reset_{CURRENT_THEME}.svg",
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{ACCENT_COLOR}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v6h6"/></svg>'
    )
    CLOSE_SVG_PATH = _svg_asset(
        f"close_{CURRENT_THEME}.svg",
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{TEXT_COLOR}" stroke-width="2.9" stroke-linecap="round"><path d="M6 6l12 12"/><path d="M18 6L6 18"/></svg>'
    )

    CHECKBOX_CSS = f"""
        QCheckBox {{
            color: {TEXT_COLOR}; font-size: 14px; spacing: 12px;
            padding: 6px 2px; background: transparent;
        }}
        QCheckBox:disabled {{ color: {SUBTLE_TEXT_COLOR}; }}
        QCheckBox::indicator {{
            width: 20px; height: 20px;
            border-radius: 7px;
            border: 2px solid {SUBTLE_TEXT_COLOR};
            background: transparent;
        }}
        QCheckBox::indicator:hover {{
            border-color: {ACCENT_COLOR};
            background: {ACCENT_TINT};
        }}
        QCheckBox::indicator:checked {{
            image: url("{CHECKMARK_SVG_PATH}");
            border-color: {ACCENT_COLOR};
            background: {ACCENT_COLOR};
        }}
    """

    COMBOBOX_CSS = f"""
        QComboBox {{
            background: {FIELD_COLOR}; color: {FIELD_TEXT_COLOR};
            border-radius: 16px; padding: 12px 16px 12px 46px; font-size: 14px;
            font-family: {ui_popup_font_family_css()};
            font-weight: 500;
            border: 1px solid transparent;
            min-height: 26px;
            selection-background-color: {ACCENT_TINT_STRONG};
            selection-color: {TEXT_COLOR};
        }}
        QComboBox:hover {{
            background: {FIELD_HOVER_COLOR};
        }}
        QComboBox:focus {{
            background: {FIELD_HOVER_COLOR};
            border: 2px solid {ACCENT_COLOR};
            padding: 11px 15px 11px 45px;
        }}
        QComboBox::drop-down {{
            subcontrol-origin: padding; subcontrol-position: center left;
            width: 38px; border: none;
            margin: 5px 0px 5px 6px;
        }}
        QComboBox::down-arrow {{
            image: url("{DROPDOWN_SVG_PATH}");
            width: 17px; height: 17px;
        }}
        QComboBox QAbstractItemView {{
            background: {MENU_BG_COLOR}; background-color: {MENU_BG_COLOR}; color: {TEXT_COLOR};
            selection-background-color: {ACCENT_TINT_STRONG}; selection-color: {TEXT_COLOR};
            border: 1px solid {SOFT_LINE_COLOR}; border-radius: 12px; outline: 0px;
            padding: 8px;
            font-family: {ui_popup_font_family_css()};
            font-size: 14px;
            font-weight: 400;
        }}
        QComboBox QAbstractItemView::item {{
            min-height: 30px; padding: 7px 12px; border-radius: 10px;
        }}
        QComboBox QAbstractItemView::item:hover {{
            background-color: {HOVER_TINT};
        }}
        QComboBox QAbstractItemView::item:selected {{
            background-color: {ACCENT_TINT_STRONG}; color: {TEXT_COLOR};
        }}
    """

    LINE_EDIT_CSS = f"""
        QLineEdit {{
            background: {FIELD_COLOR}; color: {FIELD_TEXT_COLOR};
            border-radius: 16px; padding: 12px 16px;
            border: 1px solid transparent;
            font-size: 14px;
            selection-background-color: {ACCENT_TINT_STRONG};
            selection-color: {TEXT_COLOR};
        }}
        QLineEdit:hover {{ background: {FIELD_HOVER_COLOR}; }}
        QLineEdit:focus {{ background: {FIELD_HOVER_COLOR}; border: 2px solid {ACCENT_COLOR}; padding: 11px 15px; }}
        QLineEdit:disabled {{ color: {SUBTLE_TEXT_COLOR}; background: {PANEL_COLOR}; }}
    """

    TEXT_EDIT_CSS = f"""
        QTextEdit {{
            background: {FIELD_COLOR}; color: {FIELD_TEXT_COLOR};
            border: 1px solid transparent;
            border-radius: 16px; padding: 12px;
            selection-background-color: {ACCENT_TINT_STRONG};
            selection-color: {TEXT_COLOR};
        }}
        QTextEdit:focus {{ background: {FIELD_HOVER_COLOR}; border: 2px solid {ACCENT_COLOR}; padding: 11px; }}
        QTextEdit viewport {{ background: transparent; color: {FIELD_TEXT_COLOR}; }}
    """

    PRIMARY_BUTTON_CSS = f"""
        QPushButton {{
            background: {ACCENT_COLOR};
            color: {ACCENT_TEXT_COLOR}; font-weight: 600;
            padding: 12px 24px; border-radius: 22px; font-size: 14px;
            border: none;
            outline: none;
        }}
        QPushButton:hover {{ background: {ACCENT_HOVER_COLOR}; }}
        QPushButton:pressed {{ background: {ACCENT_COLOR}; padding-top: 13px; padding-bottom: 11px; }}
        QPushButton:disabled {{ background: {PANEL_ELEVATED_COLOR}; color: {SUBTLE_TEXT_COLOR}; }}
    """

    SECONDARY_BUTTON_CSS = f"""
        QPushButton {{
            background-color: {ACCENT_TINT}; color: {ACCENT_COLOR};
            border: none; border-radius: 20px;
            padding: 10px 18px; font-size: 13px; font-weight: 600;
            outline: none;
        }}
        QPushButton:hover {{ background-color: {ACCENT_TINT_STRONG}; }}
        QPushButton:pressed {{ background-color: {ACCENT_TINT_STRONG}; }}
        QPushButton:checked {{
            background: {ACCENT_COLOR};
            color: {ACCENT_TEXT_COLOR};
        }}
        QPushButton:disabled {{ color: {SUBTLE_TEXT_COLOR}; background: transparent; }}
    """

    DANGER_BUTTON_CSS = f"""
        QPushButton {{
            background-color: rgba(229,73,58,0.12); color: {DANGER_COLOR};
            border: none;
            border-radius: 20px; padding: 10px 18px; font-weight: 600;
            outline: none;
        }}
        QPushButton:hover {{ background-color: rgba(229,73,58,0.20); }}
        QPushButton:pressed {{ background-color: rgba(229,73,58,0.28); }}
    """

    NAV_CARD_CSS = f"""
        QFrame#SettingsNavCard {{
            background: {GLASS_STRONG_COLOR};
            color: {TEXT_COLOR};
            border: 1px solid {SOFT_LINE_COLOR};
            border-radius: 24px;
        }}
        QFrame#SettingsNavCard:hover {{
            background: {PANEL_ELEVATED_COLOR};
            border-color: {LINE_COLOR};
        }}
    """

    INPUT_FRAME_CSS = f"""
        QFrame#InputFrame {{
            background: {GLASS_STRONG_COLOR};
            border: 1px solid {SOFT_LINE_COLOR};
            border-radius: 42px;
        }}
        QFrame#InputFrame:hover {{
            background: {FIELD_HOVER_COLOR};
        }}
    """

    SCROLLBAR_CSS = f"""
        QScrollBar:vertical {{ background: transparent; width: 10px; border-radius: 5px; margin: 2px 0px; }}
        QScrollBar::handle:vertical {{ background: {SUBTLE_TEXT_COLOR}; min-height: 28px; border-radius: 5px; margin: 0px 2px; }}
        QScrollBar::handle:vertical:hover {{ background: {ACCENT_COLOR}; }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0px; }}
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{ background: none; }}
        QScrollBar:horizontal {{ background: transparent; height: 10px; border-radius: 5px; margin: 0px 2px; }}
        QScrollBar::handle:horizontal {{ background: {SUBTLE_TEXT_COLOR}; min-width: 28px; border-radius: 5px; margin: 2px 0px; }}
        QScrollBar::handle:horizontal:hover {{ background: {ACCENT_COLOR}; }}
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0px; }}
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{ background: none; }}
    """

    SLIDER_CSS = f"""
        QSlider {{ min-height: 54px; }}
        QSlider::groove:horizontal {{
            height: 32px; border-radius: 16px;
            background: {PANEL_ELEVATED_COLOR};
        }}
        QSlider::sub-page:horizontal {{
            background: {ACCENT_COLOR};
            border-radius: 16px;
        }}
        QSlider::add-page:horizontal {{
            background: {PANEL_ELEVATED_COLOR};
            border-radius: 16px;
        }}
        QSlider::handle:horizontal {{
            background: transparent;
            border: none;
            width: 0px; height: 0px; margin: 0px;
        }}
        QSlider::handle:horizontal:hover {{
            background: transparent;
        }}
    """

    LOG_TEXT_CSS = f"""
        QTextEdit {{
            background: {FIELD_COLOR}; color: {FIELD_TEXT_COLOR};
            border: 1px solid {SOFT_LINE_COLOR};
            border-radius: 16px; padding: 12px;
            font-family: 'SF Mono', Menlo, Consolas, 'Courier New';
            font-size: 12px;
            selection-background-color: {ACCENT_TINT_STRONG};
            selection-color: {TEXT_COLOR};
        }}
        QTextEdit viewport {{ background: {FIELD_COLOR}; color: {FIELD_TEXT_COLOR}; }}
    """ + SCROLLBAR_CSS


def _publish_theme_to_importers():
    for module_name, module in list(sys.modules.items()):
        if not module_name.startswith("smarti.") or module_name == __name__:
            continue
        module_dict = getattr(module, "__dict__", {})
        for name in THEME_EXPORT_NAMES:
            if name in module_dict and name in globals():
                module_dict[name] = globals()[name]


def set_ui_theme(mode=None, settings=None):
    """Apply a theme to exported design tokens and already-imported Smarti modules."""
    _refresh_theme_exports(mode, settings)
    _publish_theme_to_importers()
    return CURRENT_THEME


def build_qt_palette():
    palette = QPalette()
    for group in (QPalette.ColorGroup.Active, QPalette.ColorGroup.Inactive, QPalette.ColorGroup.Disabled):
        palette.setColor(group, QPalette.ColorRole.Window, QColor(BG_COLOR))
        palette.setColor(group, QPalette.ColorRole.WindowText, QColor(TEXT_COLOR))
        palette.setColor(group, QPalette.ColorRole.Base, QColor(FIELD_COLOR))
        palette.setColor(group, QPalette.ColorRole.AlternateBase, QColor(PANEL_ELEVATED_COLOR))
        palette.setColor(group, QPalette.ColorRole.ToolTipBase, QColor(TOOLTIP_BG_COLOR))
        palette.setColor(group, QPalette.ColorRole.ToolTipText, QColor(TOOLTIP_TEXT_COLOR))
        palette.setColor(group, QPalette.ColorRole.Text, QColor(FIELD_TEXT_COLOR))
        palette.setColor(group, QPalette.ColorRole.Button, QColor(PANEL_ELEVATED_COLOR))
        palette.setColor(group, QPalette.ColorRole.ButtonText, QColor(TEXT_COLOR))
        palette.setColor(group, QPalette.ColorRole.Highlight, QColor(ACCENT_COLOR))
        palette.setColor(group, QPalette.ColorRole.HighlightedText, QColor(ACCENT_TEXT_COLOR))
    return palette


def tooltip_stylesheet():
    return (
        f"QFrame#SmartiTooltipPopup {{ background-color: {TOOLTIP_BG_COLOR}; "
        "border: none; border-radius: 8px; }"
        f"QLabel {{ color: {TOOLTIP_TEXT_COLOR}; background: transparent; "
        f"font-family: {ui_popup_font_family_css()}; font-size: 12px; font-weight: 500; "
        "padding: 7px 12px; }"
    )


def _tooltip_html(text):
    raw = str(text or "").strip()
    if not raw:
        return ""
    is_rich = bool(re.search(r"<[a-zA-Z][^>]*>", raw))
    body = raw if is_rich else html.escape(raw)
    direction = "rtl" if re.search(r"[\u0590-\u05ff]", raw) else "ltr"
    align = "right" if direction == "rtl" else "left"
    return (
        f"<div dir='{direction}' style='color:{TOOLTIP_TEXT_COLOR}; "
        f"background-color:{TOOLTIP_BG_COLOR}; text-align:{align}; "
        "white-space:normal;'>"
        f"{body}</div>"
    )


class SmartiTooltipController(QObject):
    def __init__(self, app):
        super().__init__(app)
        self.popup = QFrame(None, Qt.WindowType.ToolTip | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        self.popup.setObjectName("SmartiTooltipPopup")
        self.popup.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)
        self.popup.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.popup.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        layout = QVBoxLayout(self.popup)
        layout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel()
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setWordWrap(True)
        self.label.setMaximumWidth(360)
        layout.addWidget(self.label)
        self.hide_timer = QTimer(self)
        self.hide_timer.setSingleShot(True)
        self.hide_timer.timeout.connect(self.popup.hide)
        self.apply_theme()

    def apply_theme(self):
        self.popup.setStyleSheet(tooltip_stylesheet())
        self.label.setStyleSheet(
            f"color: {TOOLTIP_TEXT_COLOR}; background: transparent; "
            f"font-family: {ui_popup_font_family_css()}; font-size: 12px; font-weight: 500; "
            "padding: 7px 12px;"
        )

    def eventFilter(self, obj, event):
        try:
            return self._filter_event(obj, event)
        except RuntimeError:
            # The popup widget is destroyed during interpreter/app shutdown.
            return False

    def _filter_event(self, obj, event):
        if obj is self.popup or obj is self.label:
            return False
        event_type = event.type()
        if event_type == QEvent.Type.ToolTip:
            text = ""
            try:
                text = str(obj.toolTip() or "").strip()
            except Exception:
                text = ""
            if not text:
                self.popup.hide()
                return False
            self.show_tooltip(text, event.globalPos() if hasattr(event, "globalPos") else QCursor.pos())
            event.accept()
            return True
        if event_type in {
            QEvent.Type.Leave,
            QEvent.Type.MouseButtonPress,
            QEvent.Type.KeyPress,
            QEvent.Type.WindowDeactivate,
            QEvent.Type.Hide,
        }:
            if self.popup.isVisible():
                self.popup.hide()
        return False

    def show_tooltip(self, text, pos):
        html_text = _tooltip_html(text)
        if not html_text:
            self.popup.hide()
            return
        self.label.setText(html_text)
        self.label.adjustSize()
        self.popup.adjustSize()
        tooltip_size = self.popup.sizeHint()
        show_pos = QPoint(pos.x() + 12, pos.y() + 18)
        screen = QApplication.screenAt(show_pos) or QApplication.primaryScreen()
        if screen:
            available = screen.availableGeometry()
            show_pos.setX(max(available.left(), min(show_pos.x(), available.right() - tooltip_size.width())))
            show_pos.setY(max(available.top(), min(show_pos.y(), available.bottom() - tooltip_size.height())))
        self.popup.move(show_pos)
        self.popup.resize(tooltip_size)
        self.popup.show()
        self.hide_timer.start(8000)


def install_smarti_tooltips(app):
    if not app:
        return
    controller = getattr(app, "_smarti_tooltip_controller", None)
    if controller is None:
        controller = SmartiTooltipController(app)
        app.installEventFilter(controller)
        app._smarti_tooltip_controller = controller
    controller.apply_theme()


def apply_app_theme(app=None, mode=None, settings=None):
    set_ui_theme(mode, settings)
    app = app or QApplication.instance()
    if app:
        palette = build_qt_palette()
        app.setPalette(palette)
        QToolTip.setPalette(palette)
        QToolTip.setFont(app_font(10, QFont.Weight.Medium))
        stylesheet = application_stylesheet()
        # Reassigning an application stylesheet repolishes every descendant.
        # This structural stylesheet is palette-based, so a palette swap is
        # enough on theme changes even with a long chat on screen.
        if app.styleSheet() != stylesheet:
            app.setStyleSheet(stylesheet)
        install_smarti_tooltips(app)
    return CURRENT_THEME


def application_stylesheet():
    return f"""
        QWidget {{
            font-family: {ui_font_family_css()};
            color: palette(window-text);
            selection-background-color: palette(highlight);
            selection-color: palette(highlighted-text);
            {asset_font_normal_italic_widget_css()}
        }}
        QMainWindow, QDialog, QMessageBox {{
            background-color: palette(window);
            color: palette(window-text);
        }}
        QLabel {{
            color: palette(window-text);
            background: transparent;
        }}
        QTextEdit {{ cursor-move-style: logical; }}
        QLineEdit {{ cursor-move-style: logical; }}
        QPushButton, QToolButton, QCheckBox, QComboBox, QLineEdit, QTextEdit,
        QPlainTextEdit, QListWidget, QTreeWidget, QMenu, QAbstractItemView {{
            outline: none;
        }}
        QToolTip, QTipLabel {{
            background: palette(tool-tip-base);
            background-color: palette(tool-tip-base);
            color: palette(tool-tip-text);
            border: none;
            border-radius: 8px;
            padding: 7px 12px;
            font-family: {ui_popup_font_family_css()};
            font-size: 12px;
            font-weight: 500;
        }}
        QMenu {{
            background-color: palette(base);
            color: palette(text);
            border: 1px solid palette(mid);
            border-radius: 14px;
            font-family: {ui_popup_font_family_css()};
            font-size: 14px;
            font-weight: 400;
            padding: 8px;
        }}
        QMenu::item {{
            padding: 9px 30px 9px 12px;
            border-radius: 10px;
            min-width: 118px;
        }}
        QMenu::icon {{
            padding-right: 4px;
        }}
        QMenu::indicator {{
            width: 18px;
            height: 18px;
            padding-right: 4px;
        }}
        QMenu::indicator:checked {{
            image: none;
        }}
        QMenu::item:selected {{
            background-color: palette(highlight);
            color: palette(highlighted-text);
        }}
        QMenu::separator {{
            height: 1px;
            background: palette(mid);
            margin: 7px 10px;
        }}
        QDialogButtonBox QPushButton {{
            background-color: palette(button);
            color: palette(button-text);
            border: none;
            border-radius: 20px;
            padding: 10px 20px;
            font-weight: 600;
        }}
        QDialogButtonBox QPushButton:hover {{
            background-color: palette(highlight);
            color: palette(highlighted-text);
        }}
    """


def dialog_stylesheet():
    return f"""
        QDialog {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {MESH_A}, stop:0.48 {MESH_B}, stop:1 {MESH_C});
            color: {TEXT_COLOR};
        }}
        QLabel {{ color: {TEXT_COLOR}; background: transparent; }}
        QDialogButtonBox QPushButton {{
            background: {ACCENT_TINT}; color: {ACCENT_COLOR};
            border: none; border-radius: 20px;
            min-width: 76px; padding: 10px 20px; font-weight: 600;
        }}
        QDialogButtonBox QPushButton:hover {{
            background: {ACCENT_TINT_STRONG};
        }}
    """ + LINE_EDIT_CSS + COMBOBOX_CSS + TEXT_EDIT_CSS


def prepare_themed_input_dialog(dialog):
    if dialog is None:
        return dialog
    dialog.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    dialog.setOkButtonText("אישור")
    dialog.setCancelButtonText("ביטול")
    dialog.setStyleSheet(dialog_stylesheet())
    return dialog


def themed_text_input(parent, title, label, text=""):
    dialog = prepare_themed_input_dialog(QInputDialog(parent))
    dialog.setWindowTitle(str(title or ""))
    dialog.setLabelText(str(label or ""))
    dialog.setTextValue(str(text or ""))
    accepted = dialog.exec() == QDialog.DialogCode.Accepted
    return dialog.textValue(), accepted


def themed_item_input(parent, title, label, items, current=0, editable=False):
    dialog = prepare_themed_input_dialog(QInputDialog(parent))
    dialog.setWindowTitle(str(title or ""))
    dialog.setLabelText(str(label or ""))
    dialog.setComboBoxItems([str(item) for item in (items or [])])
    dialog.setComboBoxEditable(bool(editable))
    combo = dialog.findChild(QComboBox)
    if combo is not None and combo.count():
        combo.setCurrentIndex(max(0, min(int(current), combo.count() - 1)))
    accepted = dialog.exec() == QDialog.DialogCode.Accepted
    return dialog.textValue(), accepted


def menu_stylesheet():
    return f"""
        QMenu {{
            background-color: {MENU_BG_COLOR};
            color: {TEXT_COLOR};
            border: 1px solid {SOFT_LINE_COLOR};
            border-radius: 14px;
            font-family: {ui_popup_font_family_css()};
            font-size: 14px;
            font-weight: 400;
            padding: 8px;
        }}
        QMenu::item {{ padding: 9px 30px 9px 12px; border-radius: 10px; min-width: 118px; }}
        QMenu::icon {{ padding-right: 4px; }}
        QMenu::indicator {{ width: 18px; height: 18px; padding-right: 4px; }}
        QMenu::indicator:checked {{ image: url("{CHECKMARK_SVG_PATH}"); }}
        QMenu::item:selected {{ background-color: {ACCENT_TINT_STRONG}; color: {TEXT_COLOR}; }}
        QMenu::separator {{ height: 1px; background: {SOFT_LINE_COLOR}; margin: 7px 10px; }}
    """

def prepare_popup_menu(menu):
    if menu is None:
        return menu
    try:
        if IS_MACOS:
            # A translucent frameless popup lets the rounded Material-style corners show.
            menu.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
            menu.setWindowFlag(Qt.WindowType.NoDropShadowWindowHint, True)
            menu.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        else:
            # Opaque popup windows retain Windows ClearType/subpixel rendering.
            menu.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, False)
            menu.setAttribute(Qt.WidgetAttribute.WA_OpaquePaintEvent, True)
            menu.setAutoFillBackground(True)
            menu.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
            menu.setWindowFlag(Qt.WindowType.NoDropShadowWindowHint, True)
    except Exception:
        pass
    control_font = small_control_font(10, QFont.Weight.Normal)
    menu.setFont(control_font)
    menu._smarti_small_control_font = control_font
    if not hasattr(menu, "_smarti_action_font_handler"):
        def apply_action_fonts(target=menu):
            current_font = getattr(target, "_smarti_small_control_font", target.font())
            for action in target.actions():
                action.setFont(current_font)
        menu._smarti_action_font_handler = apply_action_fonts
        menu.aboutToShow.connect(apply_action_fonts)
    menu.setStyleSheet(menu_stylesheet())
    return menu


def page_title_css(size=18):
    return f"color: {TEXT_COLOR}; font-size: {int(size)}px; font-weight: 700; background: transparent;"


def section_title_css(size=16):
    return f"color: {ACCENT_COLOR}; font-size: {int(size)}px; font-weight: 700; background: transparent;"


def muted_label_css(size=12):
    return f"color: {MUTED_TEXT_COLOR}; font-size: {int(size)}px; background: transparent;"


def card_css(padding=14, radius=8):
    radius = max(20, int(radius))
    return f"""
        QFrame {{
            background: {GLASS_STRONG_COLOR};
            border: 1px solid {SOFT_LINE_COLOR};
            border-radius: {radius}px;
            padding: {int(padding)}px;
        }}
        QLabel {{ border: none; background: transparent; }}
    """


def icon_button_css(size=48, danger=False):
    color = DANGER_COLOR if danger else ACCENT_COLOR
    tint = "rgba(229,73,58,0.14)" if danger else ACCENT_TINT
    hover = "rgba(229,73,58,0.22)" if danger else HOVER_TINT
    radius = max(1, int(size / 2))
    return f"""
        QPushButton {{
            background-color: transparent;
            border: 1px solid transparent;
            border-radius: {radius}px;
            padding: 0px;
            color: {color};
            font-size: 20px;
            font-weight: 700;
            outline: none;
        }}
        QPushButton:hover {{ background-color: {hover}; border-color: {SOFT_LINE_COLOR}; }}
        QPushButton:pressed {{ background-color: {tint}; border-color: {LINE_COLOR}; }}
        QPushButton:disabled {{ color: {SUBTLE_TEXT_COLOR}; }}
    """


def ghost_button_css():
    return f"""
        QPushButton {{
            background: transparent;
            border: 1px solid transparent;
            color: {ACCENT_COLOR};
            border-radius: 20px;
            padding: 10px 16px;
            font-weight: 600;
            outline: none;
        }}
        QPushButton:hover {{ background: {ACCENT_TINT}; }}
        QPushButton:pressed {{ background: {ACCENT_TINT_STRONG}; }}
    """


def segmented_control_css():
    return f"""
        QWidget#SegmentedControl {{
            background: {GLASS_COLOR};
            border: 1px solid {SOFT_LINE_COLOR};
            border-radius: 22px;
        }}
        QPushButton {{
            background: transparent;
            border: none;
            color: {MUTED_TEXT_COLOR};
            border-radius: 18px;
            margin: 0px;
            padding: 0px 14px;
            font-size: 13px;
            font-weight: 700;
            outline: none;
            min-height: 36px;
            max-height: 36px;
        }}
        QPushButton:hover {{
            background: {HOVER_TINT};
            color: {TEXT_COLOR};
        }}
        QPushButton:checked {{
            background: {ACCENT_COLOR};
            color: {ACCENT_TEXT_COLOR};
        }}
    """


_refresh_theme_exports()

__all__ = [name for name in globals() if not name.startswith("__")]

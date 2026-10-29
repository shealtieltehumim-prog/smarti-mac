"""Print APP_VERSION from smarti/common.py (used by build_macos.sh)."""
import re

src = open("smarti/common.py", encoding="utf-8").read()
m = re.search(r"APP_VERSION\s*=\s*[\"']([^\"']+)", src)
print((m.group(1) if m else "0.87.0").lstrip("vV"))

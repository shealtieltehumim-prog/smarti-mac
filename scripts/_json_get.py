"""Print a nested JSON value: _json_get.py FILE key [key...] (used by build_macos.sh)."""
import json
import sys

data = json.load(open(sys.argv[1], encoding="utf-8"))
for key in sys.argv[2:]:
    data = data[key]
print(data)

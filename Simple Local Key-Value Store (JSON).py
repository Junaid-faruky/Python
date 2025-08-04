import json
from pathlib import Path

STORE_FILE = Path("store.json")
if STORE_FILE.exists():
    store = json.loads(STORE_FILE.read_text())
else:
    store = {}

def set_key(k, v):
    store[k] = v
    STORE_FILE.write_text(json.dumps(store, indent=2))

def get_key(k):
    return store.get(k, None)

set_key("username", "alice")
print("username =", get_key("username"))

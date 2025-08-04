import hashlib
from pathlib import Path

hashes = {}
for path in Path('.').rglob('*'):
    if path.is_file():
        h = hashlib.md5(path.read_bytes()).hexdigest()
        hashes.setdefault(h, []).append(str(path))
for h, files in hashes.items():
    if len(files) > 1:
        print("Duplicates:", files)

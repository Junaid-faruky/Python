import os
from pathlib import Path
for file in Path('.').iterdir():
    if file.is_file():
        ext = file.suffix.lower().strip('.')
        if ext:
            target = Path(ext)
            target.mkdir(exist_ok=True)
            file.rename(target / file.name)
print("Organized files by extension.")

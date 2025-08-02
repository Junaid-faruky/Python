import shutil
import datetime
import os

src = "myproject"
dst = f"backups/{os.path.basename(src)}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"

shutil.copytree(src, dst)
print(f"Backup created at {dst}")

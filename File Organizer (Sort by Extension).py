import os, shutil

path = "downloads/"
for file in os.listdir(path):
    ext = file.split(".")[-1]
    folder = os.path.join(path, ext)
    os.makedirs(folder, exist_ok=True)
    shutil.move(os.path.join(path, file), os.path.join(folder, file))

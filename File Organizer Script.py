import os, shutil

source = "Downloads"
dest = {
    "Images": [".png", ".jpg"],
    "Docs": [".pdf", ".docx"],
    "Videos": [".mp4", ".mkv"]
}

for file in os.listdir(source):
    ext = os.path.splitext(file)[1].lower()
    for folder, extensions in dest.items():
        if ext in extensions:
            shutil.move(os.path.join(source, file), os.path.join(folder, file))

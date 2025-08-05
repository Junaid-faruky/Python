import os

folder = "my_folder"
for count, filename in enumerate(os.listdir(folder)):
    ext = filename.split('.')[-1]
    new_name = f"image_{count}.{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

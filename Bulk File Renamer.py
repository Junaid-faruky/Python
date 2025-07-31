import os

folder = "test_folder"
for count, filename in enumerate(os.listdir(folder)):
    dst = f"file_{count}.txt"
    src = f"{folder}/{filename}"
    dst = f"{folder}/{dst}"
    os.rename(src, dst)
print("Files renamed successfully!")

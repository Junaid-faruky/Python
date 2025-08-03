import os
from PIL import Image
import imagehash

hashes = {}
for f in os.listdir("images"):
    if f.lower().endswith((".png", ".jpg")):
        h = imagehash.average_hash(Image.open(f))
        if str(h) in hashes:
            print(f"Duplicate: {f} and {hashes[str(h)]}")
        else:
            hashes[str(h)] = f

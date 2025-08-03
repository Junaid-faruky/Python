import os
from PIL import Image

def mock_label(image_path):
    # fake labels based on filename
    labels = []
    name = os.path.basename(image_path).lower()
    if "cat" in name: labels.append("cat")
    if "sun" in name: labels.append("sunny")
    return labels

for img in os.listdir("photos"):
    if img.lower().endswith((".jpg", ".png")):
        print(f"{img}: {mock_label('photos/'+img)}")

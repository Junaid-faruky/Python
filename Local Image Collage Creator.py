from PIL import Image
import glob

images = [Image.open(f) for f in glob.glob("images/*.jpg")[:4]]
widths, heights = zip(*(i.size for i in images))
max_width = max(widths)
total_height = sum(heights)

collage = Image.new("RGB", (max_width, total_height))
y = 0
for img in images:
    collage.paste(img, (0, y))
    y += img.height

collage.save("collage.jpg")

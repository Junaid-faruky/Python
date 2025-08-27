from PIL import Image

chars = "@%#*+=-:. "
img = Image.open("your_image.jpg").convert("L")
img = img.resize((80, 40))

ascii_art = ""
for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x, y))
        ascii_art += chars[pixel // 25]
    ascii_art += "\n"

print(ascii_art)

from PIL import Image

chars = "@%#*+=-:. "
img = Image.open("image.jpg").convert("L")
img = img.resize((100, 50))

for y in range(img.height):
    row = "".join(chars[pixel//25] for pixel in img.crop((0,y,img.width,y+1)).getdata())
    print(row)

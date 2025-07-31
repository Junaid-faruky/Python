from PIL import Image

chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def image_to_ascii(image_path, new_width=100):
    img = Image.open(image_path).convert("L")
    width, height = img.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    img = img.resize((new_width, new_height))

    pixels = img.getdata()
    ascii_str = "".join(chars[pixel//25] for pixel in pixels)
    
    ascii_img = "\n".join(ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width))
    print(ascii_img)

image_to_ascii("sample.jpg")

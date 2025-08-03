from PIL import Image

def encode(img_path, msg, out_path):
    img = Image.open(img_path)
    binary = ''.join([format(ord(c), '08b') for c in msg]) + '00000000'
    pixels = img.load()
    w, h = img.size
    idx = 0
    for y in range(h):
        for x in range(w):
            if idx >= len(binary):
                img.save(out_path)
                return
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary[idx]); idx += 1
            g = (g & ~1) | int(binary[idx]); idx += 1
            b = (b & ~1) | int(binary[idx]); idx += 1
            pixels[x, y] = (r, g, b)

encode("input.png", "Secret!", "encoded.png")

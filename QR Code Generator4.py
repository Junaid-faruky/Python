import qrcode

data = "https://github.com/yourusername"
img = qrcode.make(data)
img.save("my_qr.png")

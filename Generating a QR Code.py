# First: pip install qrcode[pil]
import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data
data = "https://www.python.org"
qr.add_data(data)
qr.make(fit=True)

# Create an image and save it
img = qr.make_image(fill_color="black", back_color="white")
img.save("python_qr.png")
print("QR code generated!")

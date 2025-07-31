import barcode
from barcode.writer import ImageWriter

data = input("Enter data for barcode: ")
code = barcode.get('code128', data, writer=ImageWriter())
code.save("barcode")

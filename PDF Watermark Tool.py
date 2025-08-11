from PyPDF2 import PdfReader, PdfWriter

pdf = PdfReader("original.pdf")
watermark = PdfReader("watermark.pdf").pages[0]
writer = PdfWriter()

for page in pdf.pages:
    page.merge_page(watermark)
    writer.add_page(page)

with open("watermarked.pdf", "wb") as f:
    writer.write(f)

print("Watermarked PDF created!")

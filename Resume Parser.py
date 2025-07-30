import pdfplumber

with pdfplumber.open("resume.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    print(text)

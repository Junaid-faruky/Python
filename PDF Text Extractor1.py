import fitz  # PyMuPDF

doc = fitz.open("sample.pdf")
for page in doc:
    print(page.get_text())

import PyPDF2

with open('file.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        print(page.extract_text())

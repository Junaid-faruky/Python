# 19. PDF reader (PyPDF2)
from PyPDF2 import PdfReader
reader = PdfReader("sample.pdf")
print(reader.pages[0].extract_text())

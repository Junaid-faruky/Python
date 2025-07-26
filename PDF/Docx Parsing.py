import os
import PyPDF2
from docx import Document

def read_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        return " ".join(page.extract_text() for page in pdf_reader.pages)

def read_docx(file_path):
    doc = Document(file_path)
    return " ".join(p.text for p in doc.paragraphs)

def extract_resume_text(file_path):
    if file_path.endswith('.pdf'):
        return read_pdf(file_path)
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    return ""

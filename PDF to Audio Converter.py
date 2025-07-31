import pyttsx3, PyPDF2
book = open('file.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
speaker = pyttsx3.init()
for page in pdfReader.pages:
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()

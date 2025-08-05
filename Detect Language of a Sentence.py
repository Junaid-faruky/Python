from langdetect import detect

text = input("Enter text: ")
print("Language:", detect(text))

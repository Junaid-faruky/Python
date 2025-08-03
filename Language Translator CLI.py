from googletrans import Translator

translator = Translator()
text = input("Text to translate: ")
dest = input("Destination language (e.g., hi for Hindi): ")
result = translator.translate(text, dest=dest)
print(f"{result.origin} -> {result.text}")

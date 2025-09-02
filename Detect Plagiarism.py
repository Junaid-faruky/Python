from difflib import SequenceMatcher

def plagiarism(a, b):
    return SequenceMatcher(None, a, b).ratio()

text1 = "Python is a great programming language"
text2 = "Python is an amazing programming language"
print(f"Similarity: {plagiarism(text1, text2)*100:.2f}%")

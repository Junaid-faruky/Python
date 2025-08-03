import regex

text = input("Enter text with emojis: ")
emoji_pattern = regex.compile(r'\X', regex.W)
counts = {}
for grapheme in emoji_pattern.findall(text):
    if any(char in emoji_pattern.findall(grapheme) for char in grapheme):
        counts[grapheme] = counts.get(grapheme, 0) + 1
print("Emoji counts:", counts)

# 3. Word Frequency Counter
from collections import Counter

text = "python is fun and python is powerful"
words = text.split()
print(Counter(words))

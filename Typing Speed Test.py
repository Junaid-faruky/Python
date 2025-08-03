import time
import random

sentences = ["The quick brown fox jumps over the lazy dog.", "Python is fun to code."]
text = random.choice(sentences)
print("Type this:", text)
start = time.time()
inp = input()
end = time.time()
wpm = (len(inp.split()) / (end - start)) * 60
print(f"WPM: {wpm:.2f}")

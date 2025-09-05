scores = {"Alice": 90, "Bob": 70, "Charlie": 85}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_scores)

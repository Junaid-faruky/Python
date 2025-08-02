import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

text = input("Enter text: ")
scores = sia.polarity_scores(text)
print("Sentiment:", scores)

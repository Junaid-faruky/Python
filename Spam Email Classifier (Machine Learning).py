from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv("spam.csv", encoding='latin-1')
df = df[['v1', 'v2']].rename(columns={"v1": "label", "v2": "text"})
tfidf = TfidfVectorizer(stop_words="english")
X = tfidf.fit_transform(df["text"])
y = df["label"].map({"ham": 0, "spam": 1})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = MultinomialNB().fit(X_train, y_train)
preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = ["This is true news", "This is fake"]
labels = [0, 1]
vec = TfidfVectorizer()
X = vec.fit_transform(texts)

clf = LogisticRegression().fit(X, labels)
print("Prediction:", clf.predict(vec.transform(["Fake example"])))

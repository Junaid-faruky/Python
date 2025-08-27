from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

train_data = ["India launches satellite", "Aliens ate my homework", "Stock market crashes"]
train_labels = ["REAL", "FAKE", "REAL"]

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_data)

model = PassiveAggressiveClassifier()
model.fit(X_train, train_labels)

test = ["Aliens are coming tomorrow!"]
X_test = vectorizer.transform(test)
print(test[0], "=>", model.predict(X_test)[0])

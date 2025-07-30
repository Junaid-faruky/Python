from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression

digits = load_digits()
model = LogisticRegression(max_iter=10000).fit(digits.data, digits.target)
print("Prediction:", model.predict([digits.data[0]]))

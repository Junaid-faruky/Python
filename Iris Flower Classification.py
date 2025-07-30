from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

data = load_iris()
model = DecisionTreeClassifier().fit(data.data, data.target)
print("Prediction:", model.predict([data.data[0]]))

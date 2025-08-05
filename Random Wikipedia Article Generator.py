import requests

res = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
data = res.json()
print(data["title"])
print(data["extract"])

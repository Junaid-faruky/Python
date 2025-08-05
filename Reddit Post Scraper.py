import requests

subreddit = "Python"
url = f"https://www.reddit.com/r/{subreddit}/hot.json"
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
for post in res.json()["data"]["children"][:5]:
    print(post["data"]["title"])

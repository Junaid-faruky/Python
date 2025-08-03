import requests
import os

token = os.getenv("GITHUB_TOKEN")
repo = "username/repo"
url = f"https://api.github.com/repos/{repo}/issues"
headers = {"Authorization": f"token {token}"}
data = {"title": "Automated Issue", "body": "Created via script"}

res = requests.post(url, json=data, headers=headers)
print("Issue URL:", res.json().get("html_url"))

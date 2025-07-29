import requests

res = requests.get("https://official-joke-api.appspot.com/random_joke").json()
print(f"{res['setup']} — {res['punchline']}")

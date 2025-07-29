import requests

base = "USD"
target = "INR"
amount = 10

url = f"https://api.exchangerate-api.com/v4/latest/{base}"
data = requests.get(url).json()
rate = data["rates"][target]
converted = amount * rate

print(f"{amount} {base} = {converted:.2f} {target}")

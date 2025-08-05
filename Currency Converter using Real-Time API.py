import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
data = requests.get(url).json()
amount = float(input("Amount in USD: "))
target = input("Convert to (e.g., INR): ").upper()
converted = amount * data['rates'][target]
print(f"{amount} USD = {converted:.2f} {target}")

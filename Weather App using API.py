import requests

city = input("Enter city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"

res = requests.get(url).json()
print(f"{city}: {res['current']['temp_c']}°C, {res['current']['condition']['text']}")

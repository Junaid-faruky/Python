import requests, time

url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"

while True:
    price = requests.get(url).json()["bpi"]["USD"]["rate"]
    print(f"BTC Price: ${price}")
    time.sleep(5)

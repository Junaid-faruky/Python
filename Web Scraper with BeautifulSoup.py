import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

for quote in soup.find_all("span", class_="text"):
    print(quote.text)

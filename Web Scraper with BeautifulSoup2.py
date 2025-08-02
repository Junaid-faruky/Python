import requests
from bs4 import BeautifulSoup

url = "https://example.com"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

for h in soup.find_all(["h1", "h2"]):
    print(h.get_text(strip=True))

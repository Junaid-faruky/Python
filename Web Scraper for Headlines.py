import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

headlines = [h.text for h in soup.find_all("h3")[:10]]
print("\n".join(headlines))

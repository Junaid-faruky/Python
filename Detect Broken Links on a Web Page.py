import requests
from bs4 import BeautifulSoup

url = input("Enter URL: ")
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
for link in soup.find_all('a', href=True):
    try:
        r = requests.head(link['href'])
        if r.status_code >= 400:
            print("Broken:", link['href'])
    except:
        print("Error:", link['href'])

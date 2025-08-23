import requests
from bs4 import BeautifulSoup

url = 'https://httpbin.org/html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the main header
header = soup.find('h1')
print(header.text)  # Output: Herman Melville - Moby-Dick

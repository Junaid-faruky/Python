import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    try:
        url = "http://quotes.toscrape.com"
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        
        print("Top Quotes:")
        for i, (quote, author) in enumerate(zip(quotes, authors), 1):
            print(f"{i}. {quote.text} - {author.text}")
            
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

scrape_quotes()

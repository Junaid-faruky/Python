# Web scraper to extract news headlines
import requests
from bs4 import BeautifulSoup

def scrape_news_headlines(url):
    try:
        # Send GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all headline elements (adjust selector as needed)
        headlines = soup.find_all('h2', class_='headline')  # Example selector
        
        print(f"Found {len(headlines)} headlines from {url}:")
        print("-" * 50)
        
        for i, headline in enumerate(headlines, 1):
            title = headline.get_text().strip()
            print(f"{i}. {title}")
            
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")

# Example usage (replace with actual news website)
scrape_news_headlines('https://example-news-website.com')

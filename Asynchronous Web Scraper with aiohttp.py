import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_multiple_sites():
    urls = [
        'https://httpbin.org/html',
        'https://httpbin.org/xml',
        'https://httpbin.org/json'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        for url, content in zip(urls, results):
            print(f"Content from {url}: {content[:200]}...")

# Run the async scraper
asyncio.run(scrape_multiple_sites())

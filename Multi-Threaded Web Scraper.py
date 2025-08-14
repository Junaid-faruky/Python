import requests
from concurrent.futures import ThreadPoolExecutor

urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts"
]

def fetch(url):
    try:
        r = requests.get(url, timeout=5)
        return f"{url} - {len(r.text)} bytes"
    except Exception as e:
        return f"{url} - Error: {e}"

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch, urls)

for res in results:
    print(res)

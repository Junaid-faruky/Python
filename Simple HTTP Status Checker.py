import requests

urls = ["https://www.google.com", "https://nonexistent.example"]
for u in urls:
    try:
        r = requests.head(u, timeout=5)
        print(f"{u}: {r.status_code}")
    except Exception as e:
        print(f"{u}: Error ({e})")

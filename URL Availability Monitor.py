import requests
import time

urls = ["https://google.com", "https://github.com"]
while True:
    for u in urls:
        try:
            r = requests.get(u, timeout=3)
            status = r.status_code
        except Exception as e:
            status = "DOWN"
        print(f"{u}: {status}")
    time.sleep(60)

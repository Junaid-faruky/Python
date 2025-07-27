# 21. Make GET request
import requests
r = requests.get("https://api.github.com")

# 22. Make POST request
r = requests.post("https://api.com", data={'key': 'value'})

# 23. Parse JSON response
data = r.json()

# 24. Custom headers
headers = {'User-Agent': 'MyApp'}
r = requests.get(url, headers=headers)

# 25. Web scraping (simple)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

# 26. Extract all links
links = [a['href'] for a in soup.find_all('a', href=True)]

# 27. File download
with open('file.txt', 'wb') as f:
    f.write(requests.get(url).content)

# 28. Upload file
files = {'file': open('file.txt', 'rb')}
r = requests.post(url, files=files)

# 29. API with auth
r = requests.get(url, auth=('user', 'pass'))

# 30. Check internet
try:
    requests.get("https://google.com")
except:
    print("Offline")

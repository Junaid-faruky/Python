import requests

# Fetch data from a public test API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
data = response.json()

print(f"Title: {data['title']}")
print(f"Body: {data['body']}")

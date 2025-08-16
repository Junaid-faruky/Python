import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status code:", response.status_code)
print("Response data:", response.json())

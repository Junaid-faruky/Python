import requests

tag = input("Enter hashtag: ")
url = f"https://www.instagram.com/explore/tags/{tag}/?__a=1"
res = requests.get(url).json()

for post in res['graphql']['hashtag']['edge_hashtag_to_media']['edges'][:5]:
    print(post['node']['edge_media_to_caption']['edges'][0]['node']['text'])

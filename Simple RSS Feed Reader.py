import feedparser

url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
feed = feedparser.parse(url)
for entry in feed.entries[:5]:
    print(entry.title)
    print(entry.link)
    print("---")

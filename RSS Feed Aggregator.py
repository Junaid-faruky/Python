import feedparser

feeds = ["https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"]
for url in feeds:
    d = feedparser.parse(url)
    for entry in d.entries[:5]:
        print(entry.title)
        print(entry.link)
        print("---")

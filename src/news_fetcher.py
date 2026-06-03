import feedparser

RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml"
]

def fetch_news():

    news=[]

    for url in RSS_FEEDS:

        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:

            news.append({
                "title":entry.title,
                "link":entry.link
            })

    return news

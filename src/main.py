from news_fetcher import fetch_news

news = fetch_news()

for item in news:
    print(item["title"])

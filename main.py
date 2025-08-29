from collections import deque
import feedparser
import asyncio
from replace_fn import replace_news
from db import insert_into_table



def get_news(link,list):
    feed = feedparser.parse(link)
    for entry in feed.entries[:20]:
        news = {'title':entry['title'],'description':entry['description']}
        list.append(news)

async def rss_parser():
    it_news = "https://habr.com/ru/rss/news/"
    news = []
    data_news = []

    get_news(it_news,news)
    replace_news(news,data_news)
    for info in data_news:
        
        try:
            insert_into_table(info["title"],info["description"],info["image"],info['url'])
            print("✅ вставлено:", info['title'])
        except Exception:
            print("❌ пропущено:", info['title'])
            continue
    

if __name__ == "__main__":
    asyncio.run(rss_parser())
    
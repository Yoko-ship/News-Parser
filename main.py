from collections import deque
import feedparser
import asyncio
from replace_fn import replace_news
from db import insert_into_table


def get_news(link,list):
    feed = feedparser.parse(link)
    for entry in feed.entries[:20]:
        news = {'title':entry['title'],'description':entry['description'],"image":entry['links'][1]['href']}
        list.append(news)

async def rss_parser():
    it_news = "https://www.it-world.ru/tech/products/rss/"
    technology_news = "https://www.it-world.ru/tech/technology/rss/"
    news = []

    while True:
        get_news(it_news,news)
        get_news(technology_news,news)
        break


    for info in news:
        try:

            insert_into_table(info["title"],info["description"],info["image"])
        except Exception:
            continue
    print("Вы успешно сохранили данные!")

if __name__ == "__main__":
    asyncio.run(rss_parser())
    
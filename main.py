import feedparser
import asyncio
from replace_fn import replace_news
from db import insert_into_table



async def get_news(link,list):
    feed = feedparser.parse(link)
    for entry in feed.entries[:10]:
        news = {'title':entry['title'],'description':entry['description']}
        list.append(news)

async def rss_parser():
    mmo_rpg = "https://www.goha.ru/rss/mmorpg"
    video_games = "https://www.goha.ru/rss/videogames"
    hardware = "https://www.goha.ru/rss/hardware"
    industry = "https://www.goha.ru/rss/industry"
    movies = "https://www.goha.ru/rss/movies-tvshows"
    news = []
    data_news = []

    await get_news(mmo_rpg,news)
    await get_news(video_games,news)
    await get_news(hardware,news)
    await get_news(industry,news)
    await get_news(movies,news)
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
    
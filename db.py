import psycopg2
from dotenv import load_dotenv
from os import getenv
load_dotenv()
DATABASE_URL = getenv("URL")
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()
cursor.execute("""
            CREATE TABLE IF NOT EXISTS news(
               id SERIAL PRIMARY KEY,
               title TEXT NOT NULL,
               description TEXT NOT NULL,
               image TEXT,
               url TEXT,
               published BOOLEAN DEFAULT FALSE,
               UNIQUE(title,description)
    )
""")



def insert_into_table(title,description,image,url):
    query = """
    INSERT INTO news(title,description,image,url) VALUES(%s,%s,%s,%s)
    """
    cursor.execute(query,(title,description,image,url))
    conn.commit()



async def get_from_table(bot,parse,channel_id):
    cursor.execute("SELECT id,title,description,image,url FROM news WHERE published = FALSE LIMIT 1")
    rows = cursor.fetchall()
    for row in rows:
        news_id,title,description,image,url = row
        caption = f"<b>{title}</b> \n\n{description} \n\n <a href='{url}'>Источник</a>"
        if image:

            await bot.send_photo(
                chat_id=channel_id,photo=image,caption=caption,parse_mode=parse,
            )
        else:
            await bot.send_message(chat_id=channel_id,text=caption,parse=parse)
        cursor.execute("UPDATE news SET published = TRUE WHERE id = %s",(news_id,))
        conn.commit()
    


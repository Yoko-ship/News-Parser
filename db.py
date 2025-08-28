import sqlite3
connection = sqlite3.connect('news.db')

cursor = connection.cursor()


cursor.execute("""
            CREATE TABLE IF NOT EXISTS news(
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               description TEXT NOT NULL,
               image TEXT,
               url TEXT,
               published INTEGER DEFAULT 0,
               UNIQUE(title,description)
    )
""")

def insert_into_table(title,description,image,url):
    query = """
    INSERT INTO news(title,description,image,url) VALUES(?,?,?,?)
    """
    cursor.execute(query,(title,description,image,url))
    connection.commit()


async def get_from_table(bot,parse,channel_id):
    cursor.execute("SELECT id,title,description,image,url FROM news WHERE published = 0 LIMIT 1")
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        news_id,title,description,image,url = row
        caption = f"<b>{title}</b> \n\n{description} \n\n <a href='{url}'>Источник</a>"
        await bot.send_photo(
            chat_id=channel_id,photo=image,caption=caption,parse_mode=parse,
        )
        cursor.execute("UPDATE news SET published = 1 WHERE id = ?",(news_id,))
        connection.commit()
    
    cursor.close()




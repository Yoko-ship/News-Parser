import sqlite3
connection = sqlite3.connect('news.db')

cursor = connection.cursor()


cursor.execute("""
            CREATE TABLE IF NOT EXISTS news(
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               description TEXT NOT NULL,
               image TEXT NOT NULL,
               UNIQUE(title,description,image)
    )
""")

def insert_into_table(title,description,image):
    query = """
    INSERT INTO news(title,description,image) VALUES(?,?,?)
    """
    cursor.execute(query,(title,description,image))
    connection.commit()


def get_from_table():
    cursor.execute("SELECT * FROM news")
    news = cursor.fetchall()
    objects = []
    for i in news:
        news_dict = {'title':i[1],"description":i[2],"image":i[3]}
        objects.append(news_dict)
    
    cursor.close()
    return objects



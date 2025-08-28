from bs4 import BeautifulSoup

def replace_news(news,data_news):
    for info in news:
            soup = BeautifulSoup(info["description"],'html.parser')
            img = soup.find("img")["src"] if soup.find('img')else None
            for tag in soup.find_all("img"):
                tag.decompose()
            
            text = soup.get_text(" ", strip=True).replace("Читать далее","")
            # print(text)

            for a in soup.find_all("a"):
                url = a.get("href")        
                data = {"title":info["title"],"description":text,"image":img,"url":url}
                data_news.append(data)
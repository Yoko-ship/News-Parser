def replace_news(news):
    replaced_news = news.replace("&#40;ADP&#41;","").replace("<br />","").replace("&nbsp;&nbsp;","")
    return replaced_news

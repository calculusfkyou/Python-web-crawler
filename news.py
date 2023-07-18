import requests
from bs4 import BeautifulSoup


def news_crawler():
    base = "https://news.cnyes.com"
    url  = "https://news.cnyes.com/news/cat/headline"
    response   = requests.get(url)

    content = ""

    # 解析網頁原始碼
    soup = BeautifulSoup(response.text, "html.parser")
    # 找到標題資料
    data = soup.find_all("a", {"class": "_1Zdp"})
    
    for index, d in enumerate(data):
        if index <8:
            title = d.text
            href  = base + d.get("href")
            content += "{}\n{}\n".format(title, href)
        else:
            break
        
    return content
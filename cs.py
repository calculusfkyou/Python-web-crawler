import requests
from bs4 import BeautifulSoup


def cs_crawler():
    base = "https://news.cnyes.com"
    url  = "https://news.cnyes.com/news/cat/headline"
    response   = requests.get(url)

    content = ""

    
    return content
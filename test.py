import requests
import logging
# log 設定
logging.basicConfig(level=logging.DEBUG)
# 向 google.com 送 HTTP Request
r = requests.get("https://www.google.com/")
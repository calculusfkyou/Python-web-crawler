import requests

url = "https://wcsie.nttu.edu.tw/" # 舉例用 url
# req_query = {"key1": "value1", "key2": ["value2", "value3"]}

r = requests.get(url) 
print(r.text)
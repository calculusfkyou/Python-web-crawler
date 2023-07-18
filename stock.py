import requests

url="https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY?"
res=requests.get(url,params={"date":"20230718","stockNo":"2330","response":"json","_":"1689640310388"})

# 把 JSON 轉成 Python 可存取之型態
res_json=res.json()
# print(res_json)

# 我們要的每日成交資訊在 data 這個欄位
daily_price_list=res_json.get("data",[])

# 該欄位是 List 所以用 for 迴圈印出
for daily_price in daily_price_list:
    print(daily_price)
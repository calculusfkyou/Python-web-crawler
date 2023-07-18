import os

# from crawl import *
from linebot.models import *
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from flask import Flask, request, abort, render_template


from news import *
from moneyNews import *
from music import *


app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi(
    '3RP6lwrPqAusQb/RUuZosPMTggjPHqnhTyde96jFZHa2RLs33bByDsWSCj+jLOEKIsluoLGlBtTibOMqY2EGXtXYBNtqvOC3VHruVIevMvs4X5ADq58/2T2kYkIhZvZwRVubH7pbZgWF5L9vGLycRgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0b81420bc205303aead84c94cfbbe564')


# handle request from "/callback" 
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# handle text message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

    # reply_token 只能用一次，用完一次就丟
    if "新聞" in message:
        result = news_crawler()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=a))
    elif "" in message:
        result = _crawler()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=b))
    elif "音樂" in message:
        result = music_crawler()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=c))
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=message))

# main
# 主程式
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
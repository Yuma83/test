from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)
import os
from private import key
import tabelog

app = Flask(__name__)

#環境変数取得
CHANNEL_ACCESS_TOKEN = key.CHANNEL_ACCESS_TOKEN()
CHANNEL_SECRET = key.CHANNEL_SECRET()

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    PATH = "./place.txt"
    if os.path.isfile(PATH):
        with open(PATH) as f:
            place = f.read()
            keyword = event.message.text
            if keyword =="なし":
                keyword = ""
            search = tabelog.Tabelog(place,keyword)
            reply_text = search.start()
            os.remove(PATH)
    else:
        with open(PATH, mode='w') as f:
            place = event.message.text
            f.write(place) 
        reply_text = "場所以外にキーワードは何かありますか？特に無ければ「なし」を入れてください。"
    
    #textがjsonタイプかtextタイプかで動作を分ける。
    if type(reply_text) == dict:
        container_obj = FlexSendMessage.new_from_json_dict(reply_text)
        line_bot_api.reply_message(event.reply_token,container_obj)
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply_text))

if __name__ == "__main__":
#    app.run()
    #port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=12345)
from flask import Flask, request, abort
import linebot
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('OsCPT7k8WkUFh/8JXZWSdxR8AKs9LQQgQhiQyGzbLlnKQJKfnFsKAai4t7XwQDNSCu7e7/BEUntlQsUN+8Bvpr0o/UAKqxOj8Ocm/LZIsR7bTLyRlZDT0hfU0/GxDzD3DwbU3PW/wZ2Tqf6jm3sfzwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('33152f3e78a40af114991b26e232dc7b')


# 監聽所有來自 /callback 的 Post Request
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


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if '蟾蜍山簡介' in msg:
        message = TextSendMessage(text="#======蟾蜍山簡介===== 1.關於蟾蜍山 2.蟾蜍山由來 3.瀏海仙翁 ")
        line_bot_api.reply_message(event.reply_token, message)
    elif '關於蟾蜍山' in msg:
        message = TextSendMessage(
            text="蟾蜍山聚落位於臺北盆地南端、臺大公館商圈旁。山城聚落內保留了都市發展的軌跡，包含清代的水利設施、日治時期的農業研究佈局、中美協防的軍事地景、臺北市目前唯一完整保留的空軍眷村「煥民新村」、結合軍眷及臺北城鄉移民的自力營造聚落等，因其豐富的歷史文化及生態資源，2014年被指定為臺北市文化景觀。"
            )
        line_bot_api.reply_message(event.reply_token, message)
    elif '蟾蜍山由來' in msg:
        message = TextSendMessage(text="蟾蜍精出現於今日台北市公館地區，據說牠經常吐出毒物毒死作物和家畜，有時甚至還會吃人，讓當地居民苦不堪言。後來呂洞賓仙公下凡成功降伏蟾蜍精，蟾蜍精就變成今日的蟾蜍山，仙跡岩上的腳印則是鬥法過程中呂仙公力道太深而留下來的。另有傳說認為降伏牠的人是劉海仙翁；或是率軍經過的鄭成功用傳說中的大砲龍碽打爛其嘴巴（或說尾巴），讓牠嚇得不敢作亂，直到公館開新路時因腳被切斷而死。"
            )
        line_bot_api.reply_message(event.reply_token, message)
    elif '瀏海仙翁' in msg:
        message = TextSendMessage(text="道教全真教 ...... 改稱瀏海。")
        line_bot_api.reply_message(event.reply_token, message)       
    elif '景點故事' in msg:
        message = ImageSendMessage(
            #放地圖
            original_content_url="https://scontent.ftpe8-1.fna.fbcdn.net/v/t1.6435-9/72642222_634082933787548_5027039107189047296_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=3mHh5UgKudUAX8IBe2B&_nc_ht=scontent.ftpe8-1.fna&oh=00_AfAcp7GMZ2_41uOQeHt6jpNO0nEdDXW8704XlBCnSTqXbQ&oe=645E4840",
            preview_image_url= "https://scontent.ftpe8-1.fna.fbcdn.net/v/t1.6435-9/72642222_634082933787548_5027039107189047296_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=3mHh5UgKudUAX8IBe2B&_nc_ht=scontent.ftpe8-1.fna&oh=00_AfAcp7GMZ2_41uOQeHt6jpNO0nEdDXW8704XlBCnSTqXbQ&oe=645E4840"
        )
        line_bot_api.reply_message(event.reply_token, message)
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '蟾蜍山地圖' in msg:
        message = LocationSendMessage(
            title='蟾蜍山',
            address='蟾蜍山',
            latitude="25.009825001671054",
            longitude="121.540005115302"
        )
        line_bot_api.reply_message(event.reply_token, message) 
    elif '開始折價挑戰' in msg:
        message = TextSendMessage(text="折價挑戰第一題 : 蟾蜍山的活動中心名稱是? (A)蟾蜍山大後院 (B)蟾蜍山大客廳 (C)蟾蜍山大舞廳")
        line_bot_api.reply_message(event.reply_token, message)  
    elif 'A' in msg:
        message = TextSendMessage(text="嗯......好像不太對喔，再想想看吧?")
        line_bot_api.reply_message(event.reply_token, message)      
    elif 'C' in msg:
        message = TextSendMessage(text="嗯......好像不太對喔，再想想看吧?")
        line_bot_api.reply_message(event.reply_token, message) 
    elif 'B' in msg:
        message = TextSendMessage(text="太棒了！回答正確，請繼續進行第二題......")
        line_bot_api.reply_message(event.reply_token, message)     
    else:
        #else : 重複用戶的發問
        message = TextSendMessage(text=msg)
        line_bot_api.reply_message(event.reply_token, message)

@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)


@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        

#if __name__ == "__main__":
#   port = int(os.environ.get('PORT', 5000))
#   app.run(host='0.0.0.0', port=port)

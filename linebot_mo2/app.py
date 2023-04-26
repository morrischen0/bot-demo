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
from linebot.models.actions import PostbackAction

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

# ======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
# ======這裡是呼叫的檔案內容=====

# ======python的函數庫==========
import tempfile
import os
import datetime
import time
# ======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(
    'OsCPT7k8WkUFh/8JXZWSdxR8AKs9LQQgQhiQyGzbLlnKQJKfnFsKAai4t7XwQDNSCu7e7/BEUntlQsUN+8Bvpr0o/UAKqxOj8Ocm/LZIsR7bTLyRlZDT0hfU0/GxDzD3DwbU3PW/wZ2Tqf6jm3sfzwdB04t89/1O/w1cDnyilFU=')
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

#--------------------------------自動發送歡迎訊息--------------------------------
@handler.add(FollowEvent)
def handle_follow(event):
    text_message1 = TextSendMessage(text='早安午安晚安~\n 我是您的蟾蜍山虛擬導遊~您可以透過點擊下方選單，得到關於蟾蜍山的一切資訊！\n 如果使用過程中，需要了解主選單的功能說明，打字輸入「選單說明」就可以囉~')
    
    text_message2 = TextSendMessage(text="蟾蜍山簡介 : 共有3種內容，將為您介紹蟾蜍山的背景知識。\n蟾蜍山地圖 : 發送蟾蜍山的google地圖資訊給您，不知道怎麼走到蟾蜍山嗎? 看這裡就對囉 \n活動資訊 : 提供蟾蜍山及大客廳的相關活動資訊給您了解 \n咖啡廳菜單 : 將咖啡廳的菜單及外送連結提供給您使用\n 景點故事&折價挑戰 : 蟾蜍山七個遊覽景點介紹，看完這些介紹並進行問答挑戰獲得咖啡廳的折扣吧!\n家輝燈 : 家輝燈也是蟾蜍山特色之一，點擊了解家輝燈的背景及設計吧")               
    
    text_message3 = TextSendMessage(text="台北市這幾年開啟了無圍牆博物館計畫，「城市是一座沒有邊界的博物館，你，身處其中，聽，臺北的聲音，故事，就在你身邊流動。」 \n https://ecomuseums.gov.taipei/Default.aspx")

    image_message = ImageSendMessage(
        original_content_url="https://i.imgur.com/uzOQLfo.jpg",
        preview_image_url="https://i.imgur.com/uzOQLfo.jpg"
    )

    line_bot_api.reply_message(event.reply_token, [text_message1,text_message2,text_message3,image_message])
#--------------------------------自動發送歡迎訊息--------------------------------

#--------------------------------處理文字訊息--------------------------------
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    #蟾蜍山簡介
    if '蟾蜍山簡介' in msg:
        message = TemplateSendMessage(
            alt_text='ButtonsTemplate',
            template=ButtonsTemplate(
                thumbnail_image_url='https://farm4.staticflickr.com/3913/14781857292_16a36268ce.jpg',
                title='蟾蜍山簡介',
                text='請選擇您所需要的介紹內容',
                actions=[
                     PostbackAction(
                         label='關於蟾蜍山',
                         data='關於蟾蜍山'
                     ),
                    PostbackAction(
                        label='蟾蜍山由來',
                        data='蟾蜍山由來'
                     ),
                    PostbackAction(
                         label='劉海仙翁',
                         data='劉海仙翁'
                     )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    #蟾蜍山地圖
    if '蟾蜍山地圖' in msg:
        message = TemplateSendMessage(
            alt_text='ButtonsTemplate',
            template=ButtonsTemplate(
                thumbnail_image_url='https://farm4.staticflickr.com/3913/14781857292_16a36268ce.jpg',
                title='蟾蜍山地圖',
                text='蟾蜍山位置 (google地圖)、蟾蜍山導覽地圖電子版',
                actions=[
                     PostbackAction(
                         label='蟾蜍山位置在哪?',
                         data='蟾蜍山位置'
                     ),
                    PostbackAction(
                        label='蟾蜍山導覽地圖電子版',
                        data='蟾蜍山導覽地圖'
                     )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    #選單說明
    if '選單說明' in msg:
        text_message1 = TextSendMessage(
            text="蟾蜍山簡介 : 共有3種內容，將為您介紹蟾蜍山的背景知識。\n蟾蜍山地圖 : 發送蟾蜍山的google地圖資訊給您，不知道怎麼走到蟾蜍山嗎? 看這裡就對囉 \n活動資訊 : 提供蟾蜍山及大客廳的相關活動資訊給您了解 \n咖啡廳菜單 : 將咖啡廳的菜單及外送連結提供給您使用\n 景點故事&折價挑戰 : 蟾蜍山七個遊覽景點介紹，看完這些介紹並進行問答挑戰獲得咖啡廳的折扣吧!\n家輝燈 : 家輝燈也是蟾蜍山特色之一，點擊了解家輝燈的背景及設計吧"
        )
        line_bot_api.reply_message(event.reply_token, text_message1)
    #活動資訊
    if '活動資訊' in msg:
        text_message1 = TextSendMessage(
            text="點擊連結，到蟾蜍山大客廳的官網上找到吸引你的精彩活動! \nhttps://huanminvillage.taipei/events"
        )
        line_bot_api.reply_message(event.reply_token, text_message1)
    
    #家輝燈
    if '家輝燈' in msg:
        text_message1 = TextSendMessage(
            text="家徽燈\n大家有沒有注意到許多蟾蜍山居民的家門口掛著一盞盞紅色的剪紙燈呢? 接下來為您介紹蟾蜍山家徽燈的由來......"
        )
        text_message2 = TextSendMessage(
            text="家徽燈源自於日本，代表著每個家族的姓氏，他們會將家族的姓氏印製在燈上，是生活文化的一部份。"
        )
        text_message3 = TextSendMessage(
            text="在蟾蜍山，陳治旭與團隊將居民的家族故事與姓氏作結合，成為與眾不同的「家徽故事燈」，之後好蟾蜍工作室發展出了「咱的故事燈」計畫。起初由剪紙藝術家陳治旭與長期關懷蟾蜍山眷村聚落的好蟾蜍工作室合作，帶領一群長期關注蟾蜍山議題的台科大設計系學生與社會人士組成團隊，透過剪紙訓練及紀錄社區故事，在半年的時間內製作出八盞家徽燈與五件故事燈。"
        )
        text_message4 = TextSendMessage(
            text="陳治旭以馬祖的風燈為發想，改變原本複雜的多面造型，運用牛奶盒四面的簡易骨架，上方糊上白棉紙，再將居民家族故事的剪紙貼上。只是社區希望作品能保存較長久的時間，於是將剪紙圖樣轉換成絹印的方式印製在布上，套入防水的牛奶盒造型骨架。陳治旭藝術家希望能持續進行家徽燈的創作，讓眷村的家族故事，像家徽燈一樣，散發出溫暖光芒。"
        )
        image_message =ImageSendMessage(
            original_content_url='https://i.imgur.com/rsplSV9.png',
            preview_image_url='https://i.imgur.com/rsplSV9.png'
        )

        line_bot_api.reply_message(event.reply_token, [text_message1,text_message2,text_message3,text_message4,image_message])

    #咖啡廳
    elif '咖啡廳菜單' in msg:
        message = TemplateSendMessage(
            alt_text='ButtonsTemplate',
            template=ButtonsTemplate(
                thumbnail_image_url='https://d1ralsognjng37.cloudfront.net/4b9787e2-2a36-4ad8-b65c-80ac479d0689.jpeg',
                title='咖啡廳菜單 & 外送訂餐',
                text='請選擇您需要的功能',
                actions=[
                    PostbackAction(
                         label='查看咖啡廳菜單',
                         data='咖啡廳菜單內容'
                     ),
                    PostbackAction(
                        label='移轉到外送訂餐頁面',
                        data='跳轉頁面',
                     )
                    
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    #景點故事七項
    if '景點故事並開始折價挑戰' in msg:
        image_message = ImageSendMessage(
        original_content_url='https://i.imgur.com/wHa8qnG.jpg',
        preview_image_url='https://i.imgur.com/wHa8qnG.jpg'
        )

        message1 = TemplateSendMessage(
            alt_text='ButtonsTemplate',
            template=ButtonsTemplate(
                thumbnail_image_url='https://mag.clab.org.tw/wp-content/uploads/2021/01/07-3.jpg',
                title='景點故事介紹',
                text='請選擇想要觀看的景點故事內容 : ',
                actions=[
                    PostbackAction(
                         label='護村神樹',
                         data='護村神樹'
                     ),
                    PostbackAction(
                        label='農試所 & 蠶改場宿舍',
                        data='農試所1',
                     ),
                    PostbackAction(
                        label='公廁',
                        data='公廁',
                     ),
                    PostbackAction(
                        label='瑠公圳造型圍欄',
                        data='造型圍欄',
                     )
                ]
            ),
            image_aspect_ratio='rectangle',
            image_size='cover',
            messages1=[image_message,template]
        )
        message2 = TemplateSendMessage(
            alt_text='ButtonsTemplate',
            template=ButtonsTemplate(
            thumbnail_image_url='https://mag.clab.org.tw/wp-content/uploads/2021/01/07-3.jpg',
                title='景點故事介紹',
                text='請選擇想要觀看的景點故事內容 : ',
                actions=[
                    PostbackAction(
                        #宿舍2故事待補
                        label='農試所宿舍2',
                        data='農試所2',
                     ),
                    PostbackAction(
                        label='夫妻樹',
                        data='夫妻樹',
                     ),
                    PostbackAction(
                        label='古道',
                        data='古道',
                     ),
                    PostbackAction(
                        label='瑠公圳',
                        data='瑠公圳',
                     )
                ]
            )
        )
        message3 = TemplateSendMessage(
            alt_text='ButtonsTemplate',
            template=ButtonsTemplate(
            thumbnail_image_url='https://mag.clab.org.tw/wp-content/uploads/2021/01/07-3.jpg',
                title='折價挑戰問答',
                text='折價挑戰問答的題目皆出自「景點故事」中的內容，共有三題，準備好了就開始吧！ ',
                actions=[
                    PostbackAction(
                         label='開始折價挑戰!',
                         data='折價挑戰'
                     ),
                    PostbackAction(
                         label='我還沒看完景點故事...還是再看一次好了',
                         data='再看景點故事'
                     ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, [message1,message2,message3])
#--------------------------------處理文字訊息--------------------------------

#---------------------------------處理選擇之後的事件---------------------------------
@handler.add(MessageEvent, message=TemplateSendMessage)
def handle_message(event):
    msg = event.message.text

    #景點故事recall
    if '再看景點故事' in msg:
        image_message = ImageSendMessage(
        original_content_url='https://i.imgur.com/wHa8qnG.jpg',
        preview_image_url='https://i.imgur.com/wHa8qnG.jpg'
        )

        message1 = TemplateSendMessage(
            alt_text='ButtonsTemplate',
            template=ButtonsTemplate(
                thumbnail_image_url='https://mag.clab.org.tw/wp-content/uploads/2021/01/07-3.jpg',
                title='景點故事介紹',
                text='請選擇想要觀看的景點故事內容 : ',
                actions=[
                    PostbackAction(
                         label='護村神樹',
                         data='護村神樹'
                     ),
                    PostbackAction(
                        #宿舍1故事改動
                        label='農試所 & 蠶改場宿舍',
                        data='農試所1',
                     ),
                    PostbackAction(
                        label='公廁',
                        data='公廁',
                     ),
                    PostbackAction(
                        label='瑠公圳造型圍欄',
                        data='造型圍欄',
                     )
                ]
            ),
            image_aspect_ratio='rectangle',
            image_size='cover',
            messages1=[image_message,template]
        )
        message2 = TemplateSendMessage(
            alt_text='ButtonsTemplate',
            template=ButtonsTemplate(
                thumbnail_image_url='https://mag.clab.org.tw/wp-content/uploads/2021/01/07-3.jpg',
                title='景點故事介紹',
                text='請選擇想要觀看的景點故事內容 : ',
                actions=[
                    PostbackAction(
                        #宿舍2故事待補
                        label='農試所宿舍2',
                        data='農試所2',
                     ),
                    PostbackAction(
                        label='夫妻樹',
                        data='夫妻樹',
                     ),
                    PostbackAction(
                        label='古道',
                        data='古道',
                     ),
                    PostbackAction(
                        label='瑠公圳',
                        data='瑠公圳',
                     )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, [message1,message2])
#---------------------------------處理選擇之後的事件---------------------------------


#---------------------------------折價遊戲函式---------------------------------
def sent_gametemp(msg):
        if msg == 'msg1':
            text_message = TextSendMessage(text="第一題 : \n\n 請問哪一個不是蟾蜍山兩棵護村神樹大樹爺爺的品種?")
            template = TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/Q2aTjmP.jpg',
                    title='折價挑戰問答',
                    text='第一題 :  ',
                    actions=[
                        PostbackAction(
                           label=' (A) 正榕',
                           data='1_A'
                        ),
                        PostbackAction(
                            label=' (B) 雀榕',
                            data='1_B'
                        ),
                        PostbackAction(
                            label=' (C) 傘榕',
                            data='1_C'
                        )
                    ]
                )
            )
            return [text_message,template]

        elif msg == 'msg2':
            text_message = TextSendMessage(text="第二題 : \n\n 請問居住在農試所的研究人員與行政人員，在完善組織合作下所進行的培育不包含以下哪項?")
            template = TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/3YKefkT.jpg',
                    title='折價挑戰問答',
                    text='第二題 :  ',
                    actions=[
                        PostbackAction(
                           label=' (A) 雞禽',
                           data='2_A'
                        ),
                        PostbackAction(
                            label=' (B) 蘋果',
                            data='2_B'
                        ),
                        PostbackAction(
                            label=' (C) 桑蠶',
                            data='2_C'
                        )
                    ]
                )
            )
            return [text_message,template]

        elif msg == 'msg3':
            text_message = TextSendMessage(text="第三題 : \n\n 請問為什麼要設計成「水」字型的造型圍欄?")
            template = TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/S7Znt1B.jpg',
                    title='折價挑戰問答',
                    text='第三題 :  ',
                    actions=[
                        PostbackAction(
                           label=' (A) 重現瑠公圳圍欄封蓋前的樣貌',
                           data='3_A'
                        ),
                        PostbackAction(
                            label=' (B) 因為附近常常淹水',
                            data='3_B'
                        ),
                        PostbackAction(
                            label=' (C) 自來水博物館在附近',
                            data='3_C'
                        )
                    ]
                )
            )
            return [text_message,template]
#---------------------------------折價遊戲函式---------------------------------

#---------------------------------處理選單選項後的事件---------------------------------
@handler.add(PostbackEvent)
def handle_message(event):
    data = event.postback.data
    #景點故事7個
    if data == '護村神樹':
        text_message = TextSendMessage(text="兩棵老樹(正榕、雀榕) 於2013年被社區提報為市定老樹，成功阻擋將要拆除眷村的怪手，因此居民匿稱他們為護村神樹。2019年台科大為兩棵老樹打開樹穴，讓大樹爺爺可以好好的喘口氣啦！")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Q2aTjmP.jpg',
            preview_image_url='https://i.imgur.com/Q2aTjmP.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message,image_message])
    elif data == '農試所1':
        text_message1 = TextSendMessage(
            text="金針菇之父宋細福\n\n在農委會大力推動下，宋細福參與了洋菇發展研究，並在洋菇市場沒落後，再投入金針菇的栽培試驗，目前全世界流行的太空包種植方式，就是他所設計的，因此有了「金針菇之父」的稱號。\n台灣金針菇的栽種在溫室環境，以及太空包栽培的技術下，打破季節和時空限制，爲台灣農業創下輝煌的歷史。"
            )
        text_message2 = TextSendMessage(
            text="洋菇之父胡開仁\n胡開仁，又稱為「臺灣洋菇之父」。出生於1921年，隨國民政府來臺，一生都在蟾蜍山農業試驗所擔任研究員。蟾蜍山農業試驗所宿舍群70號為胡開仁宿舍。\n在洋菇只能從日本進口來臺的年代，胡開仁請友人海運洋菇菌絲到臺，成功培育出臺灣自產洋菇並外銷，當年為臺灣創造出世界第一、1億美元外銷的亮眼成績。胡開仁先生一生都致力於培育洋菇，也全臺奔走教導農民們如何種植洋菇，更將「西洋菌培養法」寫成書，因而有「洋菇之父」稱號。"
            )
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/3YKefkT.jpg',
            preview_image_url='https://i.imgur.com/3YKefkT.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message1,text_message2,image_message])
    elif data == '公廁':
        text_message = TextSendMessage(text="可以稍微休息上個廁所囉~ 在早期眷村的沒有廁所，只能依賴它，現在為第四代公廁，以前僅有一半大，旁邊還有棵「金龜子樹」，可掛繩子玩盪鞦韆。在沒路燈的年代，夜晚黑壓壓一片，十分可怕！")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/zzuL4ha.jpg',
            preview_image_url='https://i.imgur.com/zzuL4ha.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message,image_message])
    elif data == '造型圍欄':
        text_message = TextSendMessage(text="猜到了嗎？這是「水」字型的圍欄，它與以前社區旁的瑠公圳圍欄相同，目前仍有幾處被保存著。")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/S7Znt1B.jpg',
            preview_image_url='https://i.imgur.com/S7Znt1B.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message,image_message])
    elif data == '農試所2':
        text_message1 = TextSendMessage(text="農試所&蠶改場宿舍第二站")
        text_message2 = TextSendMessage(text="農農業試驗所宿舍於1905年4月前在蟾蜍山下的今119巷街道旁陸續興建，養蠶所宿舍則於1910年代初期陸續設置。1958年，隨著畜產系改隸，位在半山腰的整排養豬舍則改建為農試所宿舍。隨著家庭成員增加，這些房舍的內部格局也因應需求做了改建。居住在這裡的研究人員與行政人員，在完善組織合作下所進行的菇類、花生、雞禽、柑橘、藥用植物、土壤肥料、桑蠶等的培育，為臺灣農業技術與經濟發展寫下新頁。\n隨著1977年農試所遷到霧峰、蠶業改良場遷至苗栗，宿舍所在地也於2000年因都市計畫被劃為臺灣科技大學校地，至2022年員工住戶已全數搬離。然經民間團體與原住戶的努力爭取，2018年10月15日有八棟宿舍公告為臺北市歷史建築，名稱為「農業試驗所宿舍群」及「蠶業改良所宿舍」。")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/3452TMO.jpg',
            preview_image_url='https://i.imgur.com/3452TMO.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message1,text_message2,image_message])
    elif data == '夫妻樹':
        text_message = TextSendMessage(text="舊為農試所畜產系，中庭種植的兩棵小葉南洋杉一高一矮就好像一對夫妻，因此被暱稱為「夫妻樹」，幾年前因風災倒塌一棵，過了幾年又長出來了，他們就像夫妻一樣彼此分不開。\n建築拆除後成為社區的小公園，有公共藝術與夜間太陽能照明等。")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/0NUZxSG.jpg',
            preview_image_url='https://i.imgur.com/0NUZxSG.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message,image_message])
    elif data == '古道':
        text_message = TextSendMessage(text="日治初期開關的「陸軍道」為軍隊運輸武器彈藥的路徑，在羅斯福路拓寬前曾短暫成為進出臺北盆地的主要道路。")
        image_message = ImageSendMessage(
            original_content_url='https://7.share.photo.xuite.net/mhps22/172d95d/19794561/1118706396_m.jpg',
            preview_image_url='https://7.share.photo.xuite.net/mhps22/172d95d/19794561/1118706396_m.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message,image_message])
    elif data == '瑠公圳':
        text_message = TextSendMessage(text="「我家門前有小河，後面有山坡」是過往蟾蜍山的生活寫照，沿著119巷潺潺而流的瑠公圳水質清澈，是孩子們玩水抓魚、大人洗衣游泳的好去處。\n瑠公圳為郭錫瑠（後人尊稱為瑠公」）所規劃創建。瑠公原利用陂塘開墾興雅庄一帶土地，但因陂塘只能仰賴天候積蓄雨水，加上土石淤積，於是水源漸漸不足。瑠公圳經過今景美、公館、大安區、信義區、松山等地。1970年代臺灣經濟起飛後，臺北的農地越來越少、水源也逐漸受到污染，遂加蓋轉作都市排水使用至今。")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/men4pH1.jpg',
            preview_image_url='https://i.imgur.com/men4pH1.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message,image_message])

    #蟾蜍山簡介
    if data == '關於蟾蜍山':
        text_message = TextSendMessage(text="蟾蜍山聚落位於臺北盆地南端、臺大公館商圈旁。\n山城聚落內保留了都市發展的軌跡，包含清代的水利設施、日治時期的農業研究佈局、中美協防的軍事地景、臺北市目前唯一完整保留的空軍眷村「煥民新村」、結合軍眷及臺北城鄉移民的自力營造聚落等，因其豐富的歷史文化及生態資源，2014年被指定為臺北市文化景觀。")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/uzOQLfo.jpg',
            preview_image_url='https://i.imgur.com/uzOQLfo.jpg'
        )
        line_bot_api.reply_message(event.reply_token, [text_message,image_message])

    #咖啡廳菜單2個
    if data == '咖啡廳菜單內容':
        text_message = TextSendMessage(text="請參考我們的咖啡廳菜單 : https://forms.gle/nPCF2cheKsDQpLEJ9")
        image_message = ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-F86C_BMmMYI/Xex882MsevI/AAAAAAAAUyY/yCzCFH05qBQyApsCdO5j-dzylyR-y5VgQCLcBGAsYHQ/s1600/%25E3%2580%2590%25E8%25B7%25AF%25E6%2598%2593%25E8%258E%258E%25E5%2592%2596%25E5%2595%25A1%25E3%2580%25912019%25E8%258F%259C%25E5%2596%25AE%25E5%2583%25B9%25E7%259B%25AE%25E8%25A1%25A8.jpg',
            preview_image_url='https://1.bp.blogspot.com/-F86C_BMmMYI/Xex882MsevI/AAAAAAAAUyY/yCzCFH05qBQyApsCdO5j-dzylyR-y5VgQCLcBGAsYHQ/s1600/%25E3%2580%2590%25E8%25B7%25AF%25E6%2598%2593%25E8%258E%258E%25E5%2592%2596%25E5%2595%25A1%25E3%2580%25912019%25E8%258F%259C%25E5%2596%25AE%25E5%2583%25B9%25E7%259B%25AE%25E8%25A1%25A8.jpg'
        )
        
        line_bot_api.reply_message(event.reply_token, [text_message,image_message])
    elif data == '跳轉頁面':
        text_message1 = TextSendMessage(text='點擊連結跳轉至外送平台介面點餐')
        text_message2 = TextSendMessage(text='https://www.foodpanda.com.tw/?gclid=CjwKCAjw9J2iBhBPEiwAErwpebNTXoAITefLkWhHI7mg5aCXk5TaBQW2TH2608pgm6ULBVpfcehmUBoC1N8QAvD_BwE')
 
    #蟾蜍山地圖2個
    if data == '蟾蜍山位置':
        message = LocationSendMessage(
            title='蟾蜍山',
            address='蟾蜍山',
            latitude="25.009825001671054",
            longitude="121.540005115302"
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '蟾蜍山導覽地圖':
        message = ImageSendMessage(
            # 放地圖
            original_content_url="https://scontent.ftpe8-1.fna.fbcdn.net/v/t1.6435-9/72642222_634082933787548_5027039107189047296_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=3mHh5UgKudUAX8IBe2B&_nc_ht=scontent.ftpe8-1.fna&oh=00_AfAcp7GMZ2_41uOQeHt6jpNO0nEdDXW8704XlBCnSTqXbQ&oe=645E4840",
            preview_image_url="https://scontent.ftpe8-1.fna.fbcdn.net/v/t1.6435-9/72642222_634082933787548_5027039107189047296_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=3mHh5UgKudUAX8IBe2B&_nc_ht=scontent.ftpe8-1.fna&oh=00_AfAcp7GMZ2_41uOQeHt6jpNO0nEdDXW8704XlBCnSTqXbQ&oe=645E4840"
        )
        line_bot_api.reply_message(event.reply_token, message)

    #折價挑戰
    if data == '折價挑戰':
        text_message0 = TextSendMessage(text="現在開始折價挑戰問答啦! 如果忘記了故事的話可以點擊選單再看一次景點故事噢!")
        msg = sent_gametemp('msg1')
        line_bot_api.reply_message(event.reply_token, [text_message0] + msg)

    elif data == '1_C':
        text_message0 = TextSendMessage(text="太棒了! 恭喜你答對了!請前往下一個景點繼續旅程~")
        msg = sent_gametemp('msg2')
        line_bot_api.reply_message(event.reply_token, [text_message0] + msg)

    elif data == '2_B':
        text_message0 = TextSendMessage(text="太棒了! 恭喜你答對了!請前往下一個景點繼續旅程~")
        msg = sent_gametemp('msg3')
        line_bot_api.reply_message(event.reply_token, [text_message0] + msg)

    elif data == '3_A':
        text_message0 = TextSendMessage(text="太棒了! 恭喜你完成了折價挑戰，將這則訊息向咖啡廳櫃台人員展示即可享有折扣!")
        image_message = ImageSendMessage(
            original_content_url='https://gemvg.com/wp-content/uploads/2020/03/%E8%9F%BE%E8%9C%8D%E5%B1%B1%E6%B0%B4%E5%A2%A8%E9%95%B7%E8%BB%B8.jpg',
            preview_image_url='https://gemvg.com/wp-content/uploads/2020/03/%E8%9F%BE%E8%9C%8D%E5%B1%B1%E6%B0%B4%E5%A2%A8%E9%95%B7%E8%BB%B8.jpg'
        )
        text_message1 = TextSendMessage(text="獲得折扣後千萬別急著走，可以再多使用我們的其他功能來探索蟾蜍山呦~!")
        line_bot_api.reply_message(event.reply_token, [text_message0,image_message,text_message1])

    elif data == '1_A' or data == '1_B':
        text_message0 = TextSendMessage(text="答錯了...沒關係 ! 再挑戰一次 ! 可以再看一次故事確認答案喔~")
        text_message1 = TextSendMessage(text="兩棵老樹(正榕、雀榕) 於2013年被社區提報為市定老樹，成功阻擋將要拆除眷村的怪手，因此居民匿稱他們為護村神樹。2019年台科大為兩棵老樹打開樹穴，讓大樹爺爺可以好好的喘口氣啦！")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/Q2aTjmP.jpg',
            preview_image_url='https://i.imgur.com/Q2aTjmP.jpg'
        )
        msg = sent_gametemp('msg1')
        line_bot_api.reply_message(event.reply_token, [text_message0,text_message1,image_message] + msg)

    elif data == '2_A' or data == '2_C':
        text_message0 = TextSendMessage(text="答錯了...沒關係 ! 再挑戰一次 ! 可以再看一次故事確認答案喔~")
        text_message1 = TextSendMessage(text="農試所&蠶改場宿舍第二站")
        text_message2 = TextSendMessage(text="農農業試驗所宿舍於1905年4月前在蟾蜍山下的今119巷街道旁陸續興建，養蠶所宿舍則於1910年代初期陸續設置。1958年，隨著畜產系改隸，位在半山腰的整排養豬舍則改建為農試所宿舍。隨著家庭成員增加，這些房舍的內部格局也因應需求做了改建。居住在這裡的研究人員與行政人員，在完善組織合作下所進行的菇類、花生、雞禽、柑橘、藥用植物、土壤肥料、桑蠶等的培育，為臺灣農業技術與經濟發展寫下新頁。\n隨著1977年農試所遷到霧峰、蠶業改良場遷至苗栗，宿舍所在地也於2000年因都市計畫被劃為臺灣科技大學校地，至2022年員工住戶已全數搬離。然經民間團體與原住戶的努力爭取，2018年10月15日有八棟宿舍公告為臺北市歷史建築，名稱為「農業試驗所宿舍群」及「蠶業改良所宿舍」。")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/3452TMO.jpg',
            preview_image_url='https://i.imgur.com/3452TMO.jpg'
        )
        msg = sent_gametemp('msg2')
        line_bot_api.reply_message(event.reply_token, [text_message0,text_message1,text_message2] + msg)
 
    elif data == '3_B' or data == '3_C':
        text_message0 = TextSendMessage(text="答錯了...沒關係 ! 再挑戰一次 ! 可以再看一次故事確認答案喔~")
        text_message1 = TextSendMessage(text="猜到了嗎？這是「水」字型的圍欄，它與以前社區旁的瑠公圳圍欄相同，目前仍有幾處被保存著。")
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/S7Znt1B.jpg',
            preview_image_url='https://i.imgur.com/S7Znt1B.jpg'
        )
        msg = sent_gametemp('msg3')
        line_bot_api.reply_message(event.reply_token, [text_message0,text_message1,image_message] + msg)
#---------------------------------處理選單選項後的事件---------------------------------

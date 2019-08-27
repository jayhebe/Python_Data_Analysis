# coding=utf8
from pyquery import PyQuery
from wxpy import *
import requests
import sys

sys.path.append(r"C:\Study\Programming\Python\Python_Data_Analysis")

from d12.stats_word import stats_text

wechat_bot = Bot()


@wechat_bot.register(chats=User, msg_types=SHARING)
def process_url(msg):
    content_url = msg.url
    html_code = requests.get(content_url).text
    document = PyQuery(html_code)
    content = document("#js_content").text().replace("\n", "")

    try:
        en_result, cn_result = stats_text("", content)
        # print(cn_result)
        msg.reply(cn_result)

    except ValueError as e:
        print("Exception catched.")
        print(e)


embed()

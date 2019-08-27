# coding=utf8
from pyquery import PyQuery
from wxpy import *
import requests
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(r"C:\Study\Programming\Python\Python_Data_Analysis")

from d13.stats_word import stats_text

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

        np.random.seed(20190827)
        plt.rcdefaults()
        fig, ax = plt.subplots()

        words = tuple([word for word, count in cn_result])
        y_pos = np.arange(len(words))
        performance = np.array([count for word, count in cn_result])
        error = np.random.rand(len(words))

        ax.barh(y_pos, performance, xerr=error, align="center")
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words, fontproperties='SimHei')
        ax.invert_yaxis()
        ax.set_xlabel("Frequency")
        ax.set_title("Top 20 Chinese words in an article")

        plt.show()

    except ValueError as e:
        print("Exception catched.")
        print(e)


embed()

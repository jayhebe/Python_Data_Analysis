from wxpy import *
import requests
import json


wechat_bot = Bot()


def get_reply(sentence):
    url = "http://openapi.tuling123.com/openapi/api/v2"
    userid = ""
    apikey = ""
    data = {
        "perception": {
            "inputText": {
                "text": sentence
            }
        },
        "userInfo": {
            "apiKey": apikey,
            "userId": userid
        }
    }

    turing_res = requests.post(url, data=json.dumps(data))

    return turing_res.json()["results"][0]["values"]["text"]


@wechat_bot.register(chats=User, msg_types=TEXT)
def auto_reply(msg):
    print(msg.text)
    msg_reply = get_reply(msg.text)
    print(msg_reply)
    msg.reply(msg_reply)


embed()

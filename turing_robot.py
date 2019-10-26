import requests
import json


def get_answer(sentence):
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


while True:
    dialogue = input("我：")
    print("小图：" + get_answer(dialogue))

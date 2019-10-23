import requests
import random


express_base_url = "https://www.kuaidi100.com/query"
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/71.0.3578.98 Safari/537.36'
    }

express_type = input("请输入快递名称：")
express_id = input("请输入快递单号：")
express_temp = random.random()
express_param = {
    "type": express_type,
    "postid": express_id,
    "temp": express_temp,
    "phone": ""
}

express_res = requests.get(express_base_url, headers=headers, params=express_param)
express_info = express_res.json()["data"]

if len(express_info) == 0:
    print(express_info["message"])
else:
    for info in express_info:
        print(info["time"] + " " + info["context"])

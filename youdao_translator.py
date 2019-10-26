import requests


trans_url = "http://fanyi.youdao.com/translate"
trans_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/77.0.3865.120 Safari/537.36'
}

trans_content = input("请输入你想翻译的内容：")
trans_data = {
    "i": trans_content,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
}

trans_res = requests.post(trans_url, headers=trans_headers, data=trans_data)
trans_result = trans_res.json()
print("翻译的结果为：{}".format(trans_result["translateResult"][0][0]["tgt"]))

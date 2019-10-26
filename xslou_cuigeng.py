# 小说楼登录请求：https://www.xslou.com/login.php
import requests
import json

session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/77.0.3865.120 Safari/537.36'
}


def get_cookies():
    with open("cookies.txt", "r") as f_cookies:
        cookies_dict = json.loads(f_cookies.read())

    return requests.utils.cookiejar_from_dict(cookies_dict)


def sign_in():
    url = "https://www.xslou.com/login.php"
    sign_in_data = {
        "username": input("请输入你的账号："),
        "password": input("请输入你的密码："),
        "action": "login"
    }

    session.post(url, headers=headers, data=sign_in_data)
    # print(result.status_code)
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str = json.dumps(cookies_dict)
    with open("cookies.txt", "w") as f_cookies:
        f_cookies.write(cookies_str)


def push_update(article_id):
    update_url = "https://www.xslou.com/modules/article/usercui.php"
    update_data = {
        "id": str(article_id)
    }

    return session.post(update_url, headers=headers, data=update_data)


try:
    session.cookies = get_cookies()
except:
    sign_in()
    session.cookies = get_cookies()

result = push_update(9356)
if result.status_code == 200:
    result.encoding = "gbk"
    print(result.text)

# coding=utf8
from pyquery import PyQuery
import requests
import sys
import yagmail
import getpass

sys.path.append(r"C:\Study\Programming\Python\Python_Data_Analysis")

from d11.stats_word import stats_text

content_url = "https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA"
html_code = requests.get(content_url).text
document = PyQuery(html_code)
content = document("#js_content").text().replace("\n", "")

try:
    en_result, cn_result = stats_text("", content)
    # print(cn_result)
    smtp_host = "smtp.sina.com"
    sender = input("Please enter the sender's email address: ")
    password = getpass.getpass("Please enter the sender's email password: ")
    recipient = input("Please enter the recipient's email address: ")

    yagmail.SMTP(user=sender, password=password, host=smtp_host).send(recipient, "Cutted words", str(cn_result))
except ValueError as e:
    print("Exception catched.")
    print(e)

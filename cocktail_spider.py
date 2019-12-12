from email.header import Header
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests
import random
import smtplib


youyanse_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/77.0.3865.120 Safari/537.36"
    }


def get_cocktail_urls():
    youyanse_base_url = "http://www.youyanse.com/peifang/page/"
    youyanse_page = 1
    youyanse_urls = dict()

    while True:
        youyanse_res = requests.get(youyanse_base_url + str(youyanse_page), headers=youyanse_headers)
        if youyanse_res.status_code == 200:
            youyanse_bs = BeautifulSoup(youyanse_res.text, "html.parser")
            youyanse_info = youyanse_bs.find_all("div", class_="info")
            for cocktail_link in youyanse_info:
                youyanse_urls[cocktail_link.find("h3").text.strip()] = cocktail_link.find("a")["href"]

            youyanse_page += 1
        else:
            break

    return youyanse_urls


def send_email(from_email, from_pass, to_emails, email_subject, email_body):
    smtp_server = "smtp.qq.com"

    msg = MIMEText(email_body, "html", "utf-8")
    msg['From'] = Header(from_email)
    msg['To'] = Header(to_emails)
    msg['Subject'] = Header(email_subject)

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(from_email, from_pass)
    server.sendmail(from_email, to_emails, msg.as_string())
    server.quit()


if __name__ == '__main__':
    from_addr = input("请输入发件人邮箱：")
    password = input("请输入发件人密码：")
    to_addrs = input("请输入收件人邮箱，以英文逗号分隔：")
    subject = "鸡尾酒配方"
    html_body = "<html><body>"

    cocktail_url = random.choice([url for name, url in get_cocktail_urls().items() if "52款" not in name])
    cocktail_res = requests.get(cocktail_url, headers=youyanse_headers)
    cocktail_bs = BeautifulSoup(cocktail_res.text, "html.parser")
    cocktail_name = cocktail_bs.find("h1", class_="article-title").text.strip()
    html_body += "<p>鸡尾酒名：{}<br>".format(cocktail_name)
    cocktail_info = cocktail_bs.find("div", class_="article-entry")
    cocktail_image = cocktail_info.find("div", class_="show_info").find("img")["src"]
    html_body += "<img src='{}'></p>".format(cocktail_image)
    cocktail_intro = cocktail_info.find("div", class_="show_info").text.strip()
    html_body += "<p>简短介绍：{}</p>".format(cocktail_intro)

    html_body += "<p>调酒配方：<br>"
    cocktail_recipes = cocktail_info.find("ul").find_all("li")
    for cocktail_recipe in cocktail_recipes:
        html_body += (cocktail_recipe.text.strip() + "<br>")
    html_body += "</p>"

    html_body += "<p>调酒步骤：<br>"
    cocktail_steps = cocktail_info.find("ol").find_all("li")
    for cocktail_step in cocktail_steps:
        html_body += (cocktail_step.text.strip() + "<br>")
    html_body += "</p>"

    html_body += "</body></html>"

    try:
        send_email(from_addr, password, to_addrs, subject, html_body)
        print("邮件发送成功")
    except:
        print("邮件发送失败")

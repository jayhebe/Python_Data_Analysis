from email.header import Header
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import quote
import requests
import smtplib
import random


headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }


def get_page_info(html_code):
    page_bs = BeautifulSoup(html_code, "html.parser")
    page_movies_info = page_bs.find_all("div", class_="item")
    page_next = page_bs.find("span", class_="next").find("a")
    if page_next is not None:
        page_next = page_next["href"]
    else:
        page_next = ""

    return page_movies_info, page_next


def get_movie_name():
    base_url = "https://movie.douban.com/top250"
    next_page = "?start=0&filter="
    url = base_url + next_page

    movie_names = []
    while next_page:
        page_html = requests.get(url, headers=headers)
        page_html.encoding = "utf8"
        movies_info, next_page = get_page_info(page_html.text)

        for movie_info in movies_info:
            movie_names.append(movie_info.find("span", class_="title").text)

        url = base_url + next_page

    return movie_names


def get_movie_download_link(movie_name):
    search_base_url = "http://s.ygdy8.com/plus/so.php?typeid=1&keyword="
    encode_movie_name = quote(movie_name.encode("gbk"))
    search_full_url = search_base_url + encode_movie_name

    search_res = requests.get(search_full_url)
    result_soup = BeautifulSoup(search_res.text, "html.parser")
    movie_tag = result_soup.find("div", class_="co_content8")
    movie_content = movie_tag.find("table")
    if movie_content is not None:
        movie_base_url = "http://s.ygdy8.com"
        movie_page = movie_tag.find("a")["href"]
        movie_full_url = movie_base_url + movie_page
        movie_res = requests.get(movie_full_url)
        movie_res.encoding = "gb2312"
        movie_soup = BeautifulSoup(movie_res.text, "html.parser")

        return movie_soup.find("tbody").find("a")["href"]
    else:
        return "未找到下载链接"


def send_email(from_email, from_pass, to_emails, email_subject, email_body):
    smtp_server = "smtp.qq.com"

    msg = MIMEText(email_body, "plain", "utf-8")
    msg['From'] = Header(from_email)
    msg['To'] = Header(",".join(to_emails))
    msg['Subject'] = Header(email_subject)

    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.login(from_email, from_pass)
    server.sendmail(from_email, to_emails, msg.as_string())
    server.quit()


if __name__ == '__main__':
    from_addr = input("请输入发件人邮箱：")
    password = input("请输入发件人邮箱密码：")
    to_addrs = input("请输入收件人邮箱，多个收件人用英文逗号隔开：").split(",")
    subject = "电影推荐"
    body = ""

    all_movies = get_movie_name()
    selected_movies = []
    for num in range(3):
        selected_movies.append(random.choice(all_movies))

    for movie in selected_movies:
        body += ("电影名：{}".format(movie) + "\n")
        body += ("下载链接：{}".format(get_movie_download_link(movie)) + "\n")
        body += "\n"

    send_email(from_addr, password, to_addrs, subject, body)

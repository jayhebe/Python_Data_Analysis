# coding = utf-8
import requests
import time
import random
from bs4 import BeautifulSoup

abss = "https://movie.douban.com/subject/26794435/comments"
firstPag_url = "https://movie.douban.com/subject/26794435/" \
               "comments?start=20&limit=20&sort=new_score&status=P&percent_type="
url = "https://movie.douban.com/subject/26794435/comments?start=0&limit=20&sort=new_score&status=P"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Connection': 'keep-alive'
}


def get_data(html_page):
    bs = BeautifulSoup(html_page, "html.parser")
    comment_list = bs.select('.comment > p')
    next_page = bs.select('#paginator > a')[2].get('href')
    comment_time = bs.select('..comment-time')
    return comment_list, next_page, comment_time


# def get_cookies(path):
#     # 获取cookies
#     f_cookies = open(path, 'r')
#     cookies = {}
#     for line in f_cookies.read().split(';'):  # 将Cookies字符串其转换为字典
#         name, value = line.strip().split('=', 1)
#         cookies[name] = value
#     return cookies


if __name__ == '__main__':
    # cookies = get_cookies('cookies.txt')  # cookies文件保存的前面所述的cookies
    html = requests.get(firstPag_url, headers=header).content
    comment_list, next_page, date_nodes = get_data(html)  # 首先从第一个页面处理
    soup = BeautifulSoup(html, 'lxml')
    while next_page:  # 不断的处理接下来的页面
        print(abss + next_page)
        html = requests.get(abss + next_page, headers=header).content
        # comment_list, next_page, date_nodes = get_data(html)
        soup = BeautifulSoup(html, 'lxml')
        comment_list, next_page, date_nodes = get_data(html)
        with open("comments.txt", 'a', encoding='utf-8')as f:
            for ind in range(len(comment_list)):
                comment = comment_list[ind]
                date = date_nodes[ind]
                comment = comment.get_text().strip().replace("\n", "")
                date = date.get_text().strip()
                f.writelines(date + u'\n' + comment + u'\n')
        time.sleep(1 + float(random.randint(1, 100)) / 20)

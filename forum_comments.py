import requests
from bs4 import BeautifulSoup


def get_page_info(html_code):
    page_soup = BeautifulSoup(html_code, "html.parser")
    page_next = page_soup.find(class_="next page-numbers")
    page_comments = page_soup.find_all(class_="comment-content")
    if page_next is not None:
        page_next = page_next["href"]

    return page_next, page_comments


url = "https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/comment-page-1/#comments"
while url:
    # print("Processing: {}".format(url))
    res = requests.get(url)
    url, comments = get_page_info(res.text)
    for comment in comments:
        print(comment.text)

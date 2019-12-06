from bs4 import BeautifulSoup
import requests
import os
import time


mzitu_folder_name = "mzitu_images"
mzitu_base_url = "https://www.mzitu.com/"
mzitu_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/77.0.3865.120 Safari/537.36",
    "Request": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.mzitu.com"
}


def get_page_info(url):
    res = requests.get(url, headers=mzitu_headers)
    res.encoding = res.apparent_encoding
    bs = BeautifulSoup(res.text, "html.parser")
    pics_info = bs.find("ul", id="pins").find_all("span", class_="")
    next_page = bs.find("a", class_="next page-numbers")

    return pics_info, next_page


def get_pic_url(page_url):
    mzitu_res = requests.get(page_url, headers=mzitu_headers)
    mzitu_bs = BeautifulSoup(mzitu_res.text, "html.parser")
    pic_url = mzitu_bs.find("div", class_="main-image").find("img")["src"]
    pic_pages = mzitu_bs.find("div", class_="pagenavi").find_all("a")
    pic_next_page = ""
    for pic_page in pic_pages:
        if "下一页" in pic_page.text:
            pic_next_page = pic_page["href"]

    return pic_url, pic_next_page


def get_file_name(file_extension):
    file_name = str(time.time()).replace(".", "") + file_extension
    return os.path.sep.join([os.getcwd(), mzitu_folder_name, file_name])


def download_pic(pic_url):
    print("Downloading: {}".format(pic_url))
    with open(get_file_name(".jpg"), "wb") as mzitu_fp:
        pic_content = requests.get(pic_url, headers=mzitu_headers).content
        mzitu_fp.write(pic_content)


mzitu_pics_info, mzitu_next_page = get_page_info(mzitu_base_url)
while mzitu_next_page:
    for mzitu_pic_span in mzitu_pics_info:
        mzitu_pic_next_page = mzitu_pic_span.find("a")["href"]
        # print(mzitu_pic_link["href"])
        print("Parsing page: {}".format(mzitu_pic_next_page))
        while True:
            mzitu_pic_url, mzitu_pic_next_page = get_pic_url(mzitu_pic_next_page)
            download_pic(mzitu_pic_url)
            if not mzitu_pic_next_page:
                break

    mzitu_pics_info, mzitu_next_page = get_page_info(mzitu_next_page["href"])

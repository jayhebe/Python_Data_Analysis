from bs4 import BeautifulSoup
import requests
import os
import time


meizitu_folder_name = "meizitu_images"
meizitu_base_url = "https://www.meizitu.com/a/"
meizitu_first_url = "cute_1.html"
meizitu_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/77.0.3865.120 Safari/537.36"
}


def get_page_info(url):
    res = requests.get(url, headers=meizitu_headers)
    res.encoding = res.apparent_encoding
    bs = BeautifulSoup(res.text, "html.parser")
    pic_info = bs.find_all("div", class_="pic")

    pages = bs.find("div", id="wp_page_numbers").find_all("a")
    page_info = dict()
    for page in pages:
        page_info[page.text] = page["href"]
    # print(page_info)
    if "下一页" in page_info.keys():
        next_page = page_info["下一页"]
    else:
        next_page = ""

    return pic_info, next_page


def get_file_name(file_extension):
    return str(time.time()).replace(".", "") + file_extension


meizitu_pic_info, meizitu_next_page = get_page_info(meizitu_base_url + meizitu_first_url)
while meizitu_next_page:
    for meizitu_pic in meizitu_pic_info:
        pic_link = meizitu_pic.find("a")["href"]
        pic_res = requests.get(pic_link, headers=meizitu_headers)
        pic_bs = BeautifulSoup(pic_res.text, "html.parser")
        all_pics = pic_bs.find("div", id="picture").find_all("img")
        for pic in all_pics:
            print("Processing link: {}".format(pic["src"]))
            pic_content = requests.get(pic["src"], headers=meizitu_headers).content
            with open(os.getcwd() + os.path.sep + meizitu_folder_name + get_file_name(".jpg"), "w") as meizitu_fp:
                meizitu_fp.write(pic_content)

    meizitu_pic_info, meizitu_next_page = get_page_info(meizitu_base_url + meizitu_next_page)

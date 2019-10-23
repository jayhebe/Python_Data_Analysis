# coding=utf-8

from bs4 import BeautifulSoup
from imageio import imread
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot
import string
import requests
import jieba
import sys


def get_page_info(html_code):
    page_bs = BeautifulSoup(html_code, "html.parser")
    page_comments = page_bs.select("div[style='display:;']")
    # page_next = page_bs.select("a[class='next']")
    # if len(page_next) != 0:
    #     page_next = page_next[0].get("href")

    return page_comments


def filter_text(comment):
    special_words = string.ascii_letters + \
                    string.punctuation + \
                    "！“”#$%&‘’（）*+，-。/：；、……—<=>？@[]「」【】《》^_`{|}~\n"
    for special_word in special_words:
        if special_word in comment:
            comment = comment.replace(special_word, "")

    return comment


def get_cookies(path):
    f_cookies = open(path, 'r')
    cookies = {}
    for item in f_cookies.read().split(';'):
        name, value = item.strip().split('=', 1)
        cookies[name] = value
    return cookies


def get_cutted_comments(comments):
    # comments = jieba.cut(comments, cut_all=False)
    # comments_counter = Counter()
    # for comment in comments:
    #     comments_counter[comment] += 1
    #
    # return [word for word, count in comments_counter.most_common() if len(word) >= 2]
    return jieba.cut(comments, cut_all=False)


def write_comments_to_file(page_cookies, target_file_path):
    base_url = "http://tieba.baidu.com/p/5343512726?pn="
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Connection': 'keep-alive'
    }

    for page in range(1, 39):
        new_url = base_url + str(page)
        print("Processing: ", new_url)
        html_code = requests.get(new_url, cookies=page_cookies, headers=header).content
        page_comments = get_page_info(html_code)
        print(page_comments)

        with open(target_file_path, 'a', encoding='utf-8') as f_comments:
            for page_comment in page_comments:
                f_comments.writelines(filter_text(page_comment.get_text()))


def generate_wordcloud(bg_image_path, text, target_file_path):
    os_platform = sys.platform
    if os_platform.startswith("win"):
        wc_font = r'C:\Windows\Fonts\simhei.ttf'
    elif os_platform.startswith("dar"):
        wc_font = "Hiragino Sans GB.ttc"
    else:
        wc_font = None
    wc_background_image = imread(bg_image_path)
    wc = WordCloud(collocations=False,
                   mask=wc_background_image,
                   font_path=wc_font,
                   width=1400,
                   height=1400,
                   margin=2).generate(text)
    wc_image_colors = ImageColorGenerator(wc_background_image)
    pyplot.imshow(wc.recolor(color_func=wc_image_colors))
    pyplot.axis("off")
    pyplot.figure()
    pyplot.imshow(wc_background_image, cmap=pyplot.gray())
    pyplot.axis("off")
    pyplot.show()
    wc.to_file(target_file_path)


if __name__ == '__main__':
    tieba_page_cookies = get_cookies("cookies.txt")
    target_comments_file = "comments_tieba.txt"
    target_wordcloud_file = "tieba_wordcloud.png"
    word_cloud_bg_image = "nezha.png"

    write_comments_to_file(tieba_page_cookies, target_comments_file)

    with open(target_comments_file, "rb") as f_result:
        all_comments = f_result.read()

    generate_wordcloud(word_cloud_bg_image, " ".join(get_cutted_comments(all_comments)), target_wordcloud_file)

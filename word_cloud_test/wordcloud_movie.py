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
    page_comments = page_bs.select("span[class='short']")
    page_next = page_bs.select("a[class='next']")
    if len(page_next) != 0:
        page_next = page_next[0].get("href")

    return page_comments, page_next


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


def write_comments_to_file(movie_id, page_cookies, target_file_path):
    base_url = "https://movie.douban.com/subject/" + movie_id + "/comments"
    first_url = base_url + "?start=0&limit=20&sort=new_score&status=P"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Connection': 'keep-alive'
    }

    print("Processing: ", first_url)
    html_code = requests.get(first_url, cookies=page_cookies, headers=header).content
    page_comments, page_next = get_page_info(html_code)

    while page_next:
        with open(target_file_path, 'a', encoding='utf-8') as f_comments:
            for page_comment in page_comments:
                f_comments.writelines(filter_text(page_comment.get_text()))

        new_url = base_url + page_next
        print("Processing: ", new_url)
        html_code = requests.get(new_url, cookies=page_cookies, headers=header).content
        page_comments, page_next = get_page_info(html_code)


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
    douban_movie_id = "25827935"
    douban_page_cookies = get_cookies("cookies.txt")
    target_comments_file = "comments/comments_qiyueyuansheng.txt"
    target_wordcloud_file = "wc_images/word_cloud_qiyueyuansheng.jpg"
    word_cloud_bg_image = "bg_images/qiyueyuansheng.jpg"

    write_comments_to_file(douban_movie_id, douban_page_cookies, target_comments_file)

    with open(target_comments_file, "rb") as f_result:
        all_comments = f_result.read()

    generate_wordcloud(word_cloud_bg_image, " ".join(get_cutted_comments(all_comments)), target_wordcloud_file)

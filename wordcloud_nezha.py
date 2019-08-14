from bs4 import BeautifulSoup
from collections import Counter
from imageio import imread
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot
import string
import requests
import jieba


def get_page_info(html_code):
    page_bs = BeautifulSoup(html_code, "html.parser")
    page_comments = page_bs.select("span[class='short']")
    page_next = page_bs.select("a[class='next']")[0].get("href")

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
    for line in f_cookies.read().split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    return cookies


def get_most_common_comments(comments):
    comments = jieba.cut(comments, cut_all=False)
    comments_counter = Counter()
    for comment in comments:
        comments_counter[comment] += 1

    return [word for word, count in comments_counter.most_common() if len(word) >= 2]


def generate_wordcloud(image_path, text):
    wc_font = r'C:\Windows\Fonts\FZSTK.TTF'
    wc_background_image = imread(image_path)
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
    wc.to_file('nezha_word_cloud.png')


if __name__ == '__main__':
    page_cookies = get_cookies("cookies.txt")
    # print(page_cookies)
    base_url = "https://movie.douban.com/subject/26794435/comments"
    first_url = "https://movie.douban.com/subject/26794435/comments?start=0&limit=20&sort=new_score&status=P"
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Connection': 'keep-alive'
    }

    print("Processing: ", first_url)
    html_code_nezha = requests.get(first_url, cookies=page_cookies, headers=header).content
    page_comments_nezha, page_next_nezha = get_page_info(html_code_nezha)

    while page_next_nezha:
        with open("comments_nezha.txt", 'a', encoding='utf-8') as f_nezha:
            for page_comment in page_comments_nezha:
                f_nezha.write(filter_text(page_comment.get_text()))

        new_url = base_url + page_next_nezha
        print("Processing: ", new_url)
        html_code_nezha = requests.get(new_url, cookies=page_cookies, headers=header).content
        page_comments_nezha, page_next_nezha = get_page_info(html_code_nezha)

    with open("comments_nezha.txt", "rb") as f_result:
        all_comments = f_result.read()

    most_common_comments = get_most_common_comments(all_comments)
    generate_wordcloud("bj.png", " ".join(most_common_comments))

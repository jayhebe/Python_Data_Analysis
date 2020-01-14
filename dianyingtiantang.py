import requests
from bs4 import BeautifulSoup
from urllib.request import quote


def get_movie_download_link(movie_name):
    search_base_url = "http://s.ygdy8.com/plus/s0.php?typeid=1&keyword="
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
        return ""


if __name__ == "__main__":
    download_movie_name = input("请输入你想下载的电影名称：")
    result = get_movie_download_link(download_movie_name)
    if len(result) == 0:
        print("不好意思，没有找到该电影哦")
    else:
        print("下载链接为：{}".format(result))

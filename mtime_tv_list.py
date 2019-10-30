from gevent import monkey

monkey.patch_all()

from bs4 import BeautifulSoup
from gevent.queue import Queue
import requests
import gevent
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def get_all_urls():
    url_list = []
    mtime_url = "http://www.mtime.com/top/tv/top100/"
    url_list.append(mtime_url)

    mtime_res = requests.get(mtime_url, headers=headers)
    mtime_bs = BeautifulSoup(mtime_res.text, "html.parser")

    mtime_navs = mtime_bs.find_all("a", class_="num")
    for nav in mtime_navs:
        url_list.append(nav["href"])

    return url_list


def get_movie_info(movie_url):
    movie_res = requests.get(movie_url, headers=headers)
    movie_bs = BeautifulSoup(movie_res.text, "html.parser")
    all_movie_info = movie_bs.find("div", class_="top_list").find_all("div", class_="mov_con")
    for movie_info in all_movie_info:
        movie_name = movie_info.find("h2").text
        print("电视剧名：{}".format(movie_name))

        movie_people = movie_info.find_all("p", class_="")
        for people in movie_people:
            print("{}".format(people.text))

        movie_comments = movie_info.find("p", class_="mt3")
        if movie_comments is not None:
            movie_comments = movie_comments.text
        else:
            movie_comments = ""

        print("简介：{}".format(movie_comments))
        print("-" * 30)


def run_job(job_queue):
    while not job_queue.empty():
        job_url = job_queue.get_nowait()
        get_movie_info(job_url)


if __name__ == "__main__":
    start_time = time.time()

    url_queue = Queue()
    for url in get_all_urls():
        url_queue.put_nowait(url)

    task_list = []
    for spider in range(5):
        task = gevent.spawn(run_job, url_queue)
        task_list.append(task)

    gevent.joinall(task_list)

    # for url in get_all_urls():
    #     get_movie_info(url)

    end_time = time.time()
    print(end_time - start_time)

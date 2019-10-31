from gevent import monkey

monkey.patch_all()

from gevent.queue import Queue
from bs4 import BeautifulSoup
import requests
import gevent

base_url = "http://www.boohee.com"


def get_all_urls():
    all_urls = []
    food_url = "http://www.boohee.com/food/"
    food_res = requests.get(food_url)
    food_bs = BeautifulSoup(food_res.text, "html.parser")
    food_group_urls = food_bs.find_all("div", class_="text-box")
    for food_group_url in food_group_urls:
        all_urls.append(base_url + food_group_url.find("h3").find("a")["href"])

    return all_urls


def get_page_info(group_url):
    group_res = requests.get(group_url)
    group_bs = BeautifulSoup(group_res.text, "html.parser")
    page_info = group_bs.find_all("li", class_="item clearfix")
    page_next = group_bs.find("a", class_="next_page")
    if page_next is not None:
        page_next = base_url + page_next["href"]

    return page_info, page_next


def get_all_foods(group_url):
    next_food = group_url
    while next_food:
        food_info, next_food = get_page_info(next_food)
        for food in food_info:
            food_name = food.find("h4").text.strip()
            food_link = base_url + food.find("h4").find("a")["href"]
            food_calorie = food.find("p").text.strip()

            print("食物名称：{}".format(food_name))
            print("食物链接：{}".format(food_link))
            print(food_calorie)
            print("-" * 30)


def do_jobs(event_queue):
    while not event_queue.empty():
        get_all_foods(event_queue.get_nowait())


food_url_queue = Queue()
for url in get_all_urls():
    food_url_queue.put_nowait(url)

task_list = []
for spider in range(5):
    task = gevent.spawn(do_jobs, food_url_queue)
    task_list.append(task)

gevent.joinall(task_list)

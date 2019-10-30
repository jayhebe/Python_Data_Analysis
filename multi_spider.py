from gevent import monkey
monkey.patch_all()

from gevent.queue import Queue
import gevent
import time
import requests


start_time = time.time()
url_list = [
    'https://www.baidu.com/',
    'https://www.sina.com.cn/',
    'http://www.sohu.com/',
    'https://www.qq.com/',
    'https://www.163.com/',
    'http://www.iqiyi.com/',
    'https://www.tmall.com/',
    'http://www.ifeng.com/'
]

work = Queue()
for url in url_list:
    work.put_nowait(url)


def crawler():
    while not work.empty():
        c_url = work.get_nowait()
        res = requests.get(url)
        print(c_url, work.qsize(), res.status_code)


task_list = []
for spider in range(2):
    task = gevent.spawn(crawler)
    task_list.append(task)

gevent.joinall(task_list)
end_time = time.time()
print("total: {}".format(end_time - start_time))

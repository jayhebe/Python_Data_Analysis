from ..items import Yanxuan163Item
import scrapy
import requests
import json


item_ids = []
yanxuan_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/77.0.3865.120 Safari/537.36'
}


def get_item_ids(keyword, page):
    yanxuan_params = {
        "keyword": keyword,
        "page": str(page),
        "size": "40"
    }
    base_url = "https://you.163.com/xhr/search/search.json"
    yanxuan_res = requests.get(base_url, headers=yanxuan_headers, params=yanxuan_params)
    item_result = yanxuan_res.json()["data"]["directly"]["searcherResult"]["result"]
    for item in item_result:
        item_ids.append(item["id"])

    last_page = yanxuan_res.json()["data"]["directly"]["searcherResult"]["pagination"]["lastPage"]
    if not last_page:
        get_item_ids(keyword, page + 1)


get_item_ids("文胸", 1)
# print(item_ids)


class YanxuanSpider(scrapy.Spider):
    name = "yanxuan"
    start_urls = []
    item_base_url = "https://you.163.com/xhr/comment/listByItemByTag.json?size=30&itemId="
    for item_id in item_ids:
        if item_id not in [1164006, 1164007, 1193005, 1220004, 1219004]:
            start_urls.append(item_base_url + str(item_id))

    def parse(self, response):
        item_info = json.loads(response.text)
        comment_list = item_info["data"]["commentList"]
        for comment in comment_list:
            yanxuan_item = Yanxuan163Item()
            yanxuan_item["item_id"] = comment["itemId"]
            yanxuan_item["item_color"] = comment["skuInfo"][0].split(":")[1]
            yanxuan_item["item_size"] = comment["skuInfo"][1].split(":")[1]
            yanxuan_item["item_comment"] = comment["content"]
            yanxuan_item["item_star"] = comment["star"]

            yield yanxuan_item

        item_last_page = item_info["data"]["pagination"]["lastPage"]
        if not item_last_page:
            item_url = response.request.url
            item_page = item_info["data"]["pagination"]["page"]
            if "page" in item_url:
                item_url = item_url.replace("page=" + str(item_page), "page=" + str(item_page + 1))
            else:
                item_url = item_url + "&page=" + str(item_page + 1)

            yield scrapy.Request(item_url, callback=self.parse)

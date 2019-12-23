from bs4 import BeautifulSoup
from ..items import LianjiaItem
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    start_urls = []
    base_url = "https://tj.lianjia.com/ershoufang/nankai/pg{}"
    for page in range(1, 101):
        start_urls.append(base_url.format(page))

    def parse(self, response):
        lianjia_bs = BeautifulSoup(response.text, "html.parser")
        lianjia_houses = lianjia_bs.find("ul", class_="sellListContent").find_all("li")
        for house in lianjia_houses:
            lianjia_item = LianjiaItem()
            lianjia_item["title"] = house.find("div", class_="title").find("a").text.strip()
            lianjia_item["position"] = house.find("div", class_="positionInfo").text.strip()
            lianjia_item["house_info"] = house.find("div", class_="houseInfo").text.strip()
            lianjia_item["total_price"] = house.find("div", class_="totalPrice").text.strip()
            lianjia_item["unit_price"] = house.find("div", class_="unitPrice").text.strip()
            lianjia_item["house_link"] = house.find("div", class_="title").find("a")["href"]

            yield lianjia_item

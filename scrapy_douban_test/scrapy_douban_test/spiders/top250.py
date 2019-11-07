from bs4 import BeautifulSoup
from ..items import ScrapyDoubanTestItem
import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/top250?start=0"]

    def parse(self, response):
        bs = BeautifulSoup(response.text, "html.parser")
        datas = bs.find_all("tr", class_="item")
        for data in datas:
            item = ScrapyDoubanTestItem()
            item["title"] = data.find_all("a")[1]["title"]
            item["publish"] = data.find("p", class_="pl").text
            item["score"] = data.find("span", class_="rating_nums").text
            print(item["title"])
            yield item

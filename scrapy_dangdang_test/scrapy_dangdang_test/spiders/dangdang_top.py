from bs4 import BeautifulSoup
from ..items import ScrapyDangdangTestItem
import scrapy


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    base_url = "http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-"
    start_urls = []
    for page_num in range(1, 4):
        start_urls.append(base_url + str(page_num))

    def parse(self, response):
        dangdang_bs = BeautifulSoup(response.text, "html.parser")
        book_list = dangdang_bs.find("ul", class_="bang_list clearfix bang_list_mode").find_all("li")
        for book in book_list:
            book_item = ScrapyDangdangTestItem()
            book_item["book_name"] = book.find("div", class_="name").text
            book_item["book_author"] = book.find("div", class_="publisher_info").text
            book_item["book_price"] = book.find("span", class_="price_n").text

            yield book_item

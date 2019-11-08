from bs4 import BeautifulSoup
from ..items import DoubanCommentsItem
import scrapy


class DoubanComments(scrapy.Spider):
    name = "doubancomments"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/top250?start=0", "https://book.douban.com/top250?start=25"]

    def parse(self, response):
        books_bs = BeautifulSoup(response.text, "html.parser")
        all_books = books_bs.find_all("div", class_="pl2")
        for book_info in all_books:
            book_url = book_info.find("a")["href"] + "comments"
            yield scrapy.Request(book_url, callback=self.parse_comment)

    def parse_comment(self, response):
        book_comment_bs = BeautifulSoup(response.text, "html.parser")
        book_name = book_comment_bs.find("div", id="content").find("h1").text.split()[0]
        book_comments = book_comment_bs.find_all("li", class_="comment-item")
        for book_comment in book_comments:
            douban_comment_item = DoubanCommentsItem()
            user_id = book_comment.find("span", class_="comment-info").find("a").text.strip()
            comment = book_comment.find("span", class_="short").text.strip()

            douban_comment_item["book_name"] = book_name
            douban_comment_item["user_id"] = user_id
            douban_comment_item["book_comment"] = comment

            yield douban_comment_item

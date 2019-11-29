from ..items import JuziDeathCompanyItem
import scrapy
import json


class JuziSpider(scrapy.Spider):
    name = "juzi"
    base_url = "https://www.itjuzi.com/api/closure?com_prov=&sort=&keyword=&cat_id=&page="
    start_urls = []

    for page in range(1, 629):
        start_urls.append(base_url + str(page))

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        juzi_json = json.loads(response.text)
        company_info = juzi_json["data"]["info"]
        for info in company_info:
            juzi_item = JuziDeathCompanyItem()
            juzi_item["company_name"] = info["com_name"]
            juzi_item["start_date"] = info["born"]
            juzi_item["close_date"] = info["com_change_close_date"]
            juzi_item["live_time"] = info["live_time"]
            juzi_item["business"] = info["cat_name"]
            juzi_item["location"] = info["com_prov"]
            juzi_item["fund_status"] = info["com_fund_status_name"]
            juzi_item["total_money"] = info["total_money"]

            yield juzi_item

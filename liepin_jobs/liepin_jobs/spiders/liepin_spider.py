from bs4 import BeautifulSoup
from ..items import LiepinJobsItem
import scrapy


class LiepinSpider(scrapy.Spider):
    name = "liepin"

    def start_requests(self):
        liepin_url = "https://www.liepin.com/city-bj/zhaopin/?key=%E4%BC%9A%E8%AE%A1"
        yield scrapy.Request(liepin_url, callback=self.parse)

    def parse(self, response):
        liepin_base_url = "https://www.liepin.com"
        liepin_bs = BeautifulSoup(response.text, "html.parser")
        liepin_jobs = liepin_bs.find_all("div", class_="sojob-item-main clearfix")
        liepin_next_page = liepin_bs.find("div", class_="pagerbar").find_all("a", class_="")[-1]
        for liepin_job in liepin_jobs:
            liepin_item = LiepinJobsItem()
            liepin_job_info = liepin_job.find("div", class_="job-info")
            liepin_company_info = liepin_job.find("div", class_="company-info")
            liepin_item["job_company"] = liepin_company_info.find("a").text.strip()
            liepin_item["job_industry"] = liepin_company_info.find("p", class_="field-financing").text.strip()
            liepin_item["job_title"] = liepin_job_info.find("span", class_="job-name").text.strip()
            liepin_item["job_salary"] = liepin_job_info.find("span", class_="text-warning").text.strip()
            liepin_job_area_a = liepin_job_info.find("a", class_="area")
            liepin_job_area_span = liepin_job_info.find("span", class_="area")
            liepin_job_area = liepin_job_area_a if liepin_job_area_a else liepin_job_area_span
            liepin_item["job_location"] = liepin_job_area.text.strip()
            liepin_item["job_education"] = liepin_job_info.find("span", class_="edu").text.strip()
            liepin_item["job_experience"] = liepin_job_info.find("span", class_="").text.strip()
            liepin_item["job_link"] = liepin_job_info.find("a")["href"]

            yield liepin_item

        if liepin_next_page.text.strip() == "下一页":
            liepin_next_url = liepin_base_url + liepin_next_page["href"]
            yield scrapy.Request(liepin_next_url, callback=self.parse)

from bs4 import BeautifulSoup
from ..items import ScrapyJobuiTestItem
import scrapy


class JobuiSpider(scrapy.Spider):
    name = "jobui"
    allowd_domains = ["www.jobui.com"]
    start_urls = ["https://www.jobui.com/rank/company/"]

    def parse(self, response):
        base_url = "https://www.jobui.com"
        company_bs = BeautifulSoup(response.text, "html.parser")
        company_uls = company_bs.find_all("ul", class_="textList flsty cfix")
        for company_ul in company_uls:
            company_as = company_ul.find_all("a")
            for company_a in company_as:
                company_url = base_url + company_a["href"] + "jobs"

                yield scrapy.Request(company_url, callback=self.parse_job)

    def parse_job(self, response):
        job_bs = BeautifulSoup(response.text, "html.parser")
        company_name = job_bs.find("h1", id="companyH1").text.strip()
        job_contents = job_bs.find_all("div", class_="job-simple-content")
        for job_content in job_contents:
            job_item = ScrapyJobuiTestItem()
            job_item["company_name"] = company_name
            job_item["job_title"] = job_content.find("h3").text.strip()
            job_item["job_location"] = job_content.find_all("span")[0].text.strip()
            job_item["job_description"] = job_content.find_all("span")[1].text.strip()

            yield job_item

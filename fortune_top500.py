from bs4 import BeautifulSoup
import requests
import openpyxl
import os


fortune_wb = openpyxl.Workbook()
fortune_sheet = fortune_wb.active
fortune_sheet.title = "Fortune Top 500"
fortune_sheet.append(["2019年排名", "2018年排名", "公司名称", "营业收入（百万美元）", "利润（百万美元）", "国家"])

fortune_url = "http://www.fortunechina.com/fortune500/c/2019-07/22/content_339535.htm"
fortune_res = requests.get(fortune_url)
fortune_res.encoding = fortune_res.apparent_encoding
fortune_bs = BeautifulSoup(fortune_res.text, "html.parser")
fortune_items = fortune_bs.find("tbody").find_all("tr")

for item in fortune_items:
    fortune_records = item.find_all("td")
    ranking2019 = fortune_records[0].text.strip()
    ranking2018 = fortune_records[1].text.strip()
    company = fortune_records[2].text.strip()
    income = fortune_records[3].text.strip()
    profit = fortune_records[4].text.strip()
    country = fortune_records[5].text.strip()

    fortune_sheet.append([ranking2019, ranking2018, company, income, profit, country])

filename = os.getcwd() + os.path.sep + "fortune_top500.xlsx"
fortune_wb.save(filename)

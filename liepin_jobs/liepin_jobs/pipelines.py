# -*- coding: utf-8 -*-
import openpyxl
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class LiepinJobsPipeline(object):
    def __init__(self):
        self.liepin_wb = openpyxl.Workbook()
        self.liepin_sheet = self.liepin_wb.active
        self.liepin_sheet.append(["职位名称", "公司名称", "所属行业", "薪资", "工作地点", "学历", "工作经验", "链接"])

    def process_item(self, item, spider):
        self.liepin_sheet.append([
            item["job_title"],
            item["job_company"],
            item["job_industry"],
            item["job_salary"],
            item["job_location"],
            item["job_education"],
            item["job_experience"],
            item["job_link"]
        ])
        return item

    def close_spider(self, spider):
        self.liepin_wb.save(os.getcwd() + os.path.sep + "liepin_info.xlsx")
        self.liepin_wb.close()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl
import os


class LianjiaPipeline(object):
    def __init__(self):
        self.lianjia_wb = openpyxl.Workbook()
        self.lianjia_sheet = self.lianjia_wb.active
        self.lianjia_sheet.title = "lianjia - tianjin"
        self.lianjia_sheet.append(["名称", "地点", "房屋信息", "总价", "单价", "链接"])

    def process_item(self, item, spider):
        self.lianjia_sheet.append([
                item["title"],
                item["position"],
                item["house_info"],
                item["total_price"],
                item["unit_price"],
                item["house_link"]
            ])

        return item

    def close_spider(self, spider):
        file_name = "lianjia_tianjin.xlsx"
        self.lianjia_wb.save(os.getcwd() + os.path.sep + file_name)
        self.lianjia_wb.close()

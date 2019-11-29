# -*- coding: utf-8 -*-
import openpyxl
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Yanxuan163Pipeline(object):
    def __init__(self):
        self.yanxuan_wb = openpyxl.Workbook()
        self.yanxuan_sheet = self.yanxuan_wb.active
        self.yanxuan_sheet.append(["ID", "颜色", "尺码", "评论", "评分"])

    def process_item(self, item, spider):
        self.yanxuan_sheet.append([
            item["item_id"],
            item["item_color"],
            item["item_size"],
            item["item_comment"],
            item["item_star"],
        ])
        return item

    def close_spider(self, spider):
        self.yanxuan_wb.save(os.getcwd() + os.path.sep + "yanxuan_info.xlsx")
        self.yanxuan_wb.close()

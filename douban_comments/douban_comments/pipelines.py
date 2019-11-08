# -*- coding: utf-8 -*-
import openpyxl
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanCommentsPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.append(["书名", "用户ID", "短评内容"])

    def process_item(self, item, spider):
        line = [item["book_name"], item["user_id"], item["book_comment"]]
        self.sheet.append(line)

        return item

    def close_spider(self, spider):
        self.wb.save(r".\douban_comments.xlsx")
        self.wb.close()

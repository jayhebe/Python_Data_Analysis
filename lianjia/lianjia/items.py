# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    title = scrapy.Field()
    position = scrapy.Field()
    house_info = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    house_link = scrapy.Field()

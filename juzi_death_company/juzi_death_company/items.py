# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JuziDeathCompanyItem(scrapy.Item):
    company_name = scrapy.Field()
    start_date = scrapy.Field()
    close_date = scrapy.Field()
    live_time = scrapy.Field()
    business = scrapy.Field()
    location = scrapy.Field()
    fund_status = scrapy.Field()
    total_money = scrapy.Field()

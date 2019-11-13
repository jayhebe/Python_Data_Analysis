# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinJobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()
    job_company = scrapy.Field()
    job_industry = scrapy.Field()
    job_salary = scrapy.Field()
    job_location = scrapy.Field()
    job_education = scrapy.Field()
    job_experience = scrapy.Field()
    job_link = scrapy.Field()

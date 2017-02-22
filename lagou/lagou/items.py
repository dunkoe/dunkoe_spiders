# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    lagou_id = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    tag = scrapy.Field()
    description = scrapy.Field()
    advantage = scrapy.Field()
    cpn_name = scrapy.Field()
    cpn_finance_round = scrapy.Field()
    cpn_scale = scrapy.Field()
    cpn_field = scrapy.Field()
    cpn_web_page = scrapy.Field()
    employ_type = scrapy.Field()
    biz_area = scrapy.Field()
    address = scrapy.Field()

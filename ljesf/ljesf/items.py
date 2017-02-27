# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjesfItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    link = scrapy.Field()  # 链接
    microdistrict = scrapy.Field()  # 小区
    layout = scrapy.Field()  # 户型
    area = scrapy.Field()  # 面积
    direction = scrapy.Field()  # 朝向
    fitment = scrapy.Field()  # 装修
    lift = scrapy.Field()  # 是否有电梯
    floor_count = scrapy.Field()  # 层数
    height_type = scrapy.Field()  # 高层低层
    year = scrapy.Field()  # 年份
    region = scrapy.Field()  # 附近商区
    publish_time = scrapy.Field()  # 发布时间
    focus_count = scrapy.Field()  # 关注数
    watch_count = scrapy.Field()  # 带看次数
    price = scrapy.Field()  # 价格
    per_price = scrapy.Field()  # 单价

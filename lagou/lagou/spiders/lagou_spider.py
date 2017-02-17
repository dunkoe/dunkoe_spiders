# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
# PyCharm open dunkoe_spiders as root will raise an Error, Ignore
# noinspection PyUnresolvedReferences
from lagou.items import LagouItem

# noinspection PyMethodMayBeStatic
from scrapy.spiders import Rule

from misc.dspider import DSpider
import logging


class LagouSpider(DSpider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'https://www.lagou.com/',
        # 'https://www.lagou.com/zhaopin/duomeitishejishi/',
        # 'https://www.lagou.com/jobs/2769011.html',
    )

    # def parse(self, response):
    # self.parse_boot(response=response)
    # self.parse_item(response=response)
    # self.parse_detail(response=response)
    rules = (
        Rule(LinkExtractor(allow="/jobs/[0-9]+\.html"), callback='parse_3', follow=False),
        Rule(LinkExtractor(allow="/zhaopin/.*/"), follow=True),
    )

    def parse_3(self, response):
        lagou_loader = ItemLoader(item=LagouItem(), response=response)
        lagou_loader.add_xpath('title',
                               "//div[contains(@class, 'ceil')]/span[contains(@class,'ceil-job')]/text()")

        return lagou_loader.load_item()

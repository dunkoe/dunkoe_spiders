# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
# PyCharm open dunkoe_spiders as root will raise an Error, Ignore
# noinspection PyUnresolvedReferences
from lagou.items import LagouItem

# noinspection PyMethodMayBeStatic
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapy.spiders import Rule

from misc.dspider import DSpider
import logging


class LagouLoader(ItemLoader):
    default_input_processor = TakeFirst()
    # title_in = MapCompose(unicode.strip)
    # title_out = Join()


# noinspection PyMethodMayBeStatic
class LagouSpider(DSpider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'https://www.lagou.com/',
    )

    rules = (
        Rule(LinkExtractor(allow="/jobs/[0-9]+\.html"), callback='parse_1', follow=False),
        Rule(LinkExtractor(allow="/zhaopin/.*/.*"), follow=True),
    )

    def parse_1(self, response):
        lagou_loader = LagouLoader(item=LagouItem(), response=response)
        lagou_loader.add_xpath('title',
                               "//div[contains(@class, 'ceil')]/span[contains(@class,'ceil-job')]/text()")
        # lagou_loader.add_xpath('lagou_id',"")
        lagou_loader.add_xpath('salary',
                               "//div[contains(@class, 'position-content-l')]/dd[contains(@class,'job_request')]/p/span[1]/text()")
        lagou_loader.add_xpath('city',
                               "//div[contains(@class, 'position-content-l')]/dd[contains(@class,'job_request')]/p/span[2]/text()")
        lagou_loader.add_xpath('experience',
                               "//div[contains(@class, 'position-content-l')]/dd[contains(@class,'job_request')]/p/span[3]/text()")
        lagou_loader.add_xpath('education',
                               "//div[contains(@class, 'position-content-l')]/dd[contains(@class,'job_request')]/p/span[4]/text()")
        lagou_loader.add_xpath('employ_type',
                               "//div[contains(@class, 'position-content-l')]/dd[contains(@class,'job_request')]/p/span[5]/text()")
        lagou_loader.add_xpath('tag', "//ul[contains(@class, 'position-label')]/li[contains(@class, 'labels')]/text()")
        lagou_loader.add_xpath('advantage', "//dd[contains(@class, 'job-advantage')]/p[1]/text()")
        lagou_loader.add_xpath('district', "//div[contains(@class, 'work_addr')]/a/text()")
        lagou_loader.add_xpath('description', "//dd[contains(@class, 'job-bt')]/div//text()")
        lagou_loader.add_xpath('cpn_name', "//dl[contains(@class, 'job_company')]//h2[contains(@class, 'fl')]/text()")
        lagou_loader.add_xpath('cpn_finance_round', "//dl[contains(@class, 'job_company')]/ul[contains(@class, 'c_feature')]/li[2]/text()")
        lagou_loader.add_xpath('cpn_scale', "//dl[contains(@class, 'job_company')]/ul[contains(@class, 'c_feature')]/li[3]/text()")
        lagou_loader.add_xpath('cpn_field', "//dl[contains(@class, 'job_company')]/ul[contains(@class, 'c_feature')]/li[1]/text()")
        lagou_loader.add_xpath('cpn_field', "//dl[contains(@class, 'job_company')]/ul[contains(@class, 'c_feature')]/li[4]/text()")
        return lagou_loader.load_item()

# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
# PyCharm open dunkoe_spiders as root will raise an Error, Ignore
# noinspection PyUnresolvedReferences
from lagou.items import LagouItem

# noinspection PyMethodMayBeStatic
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Identity
from scrapy.spiders import Rule

from misc.dspider import DSpider
import logging


def filter_line_diagonal(value):
    value = value.strip().strip('/').strip()
    if value != '':
        return value


def filter_line_combine(value):
    value = value.strip().strip('-').strip()
    if value != '':
        return value


class LagouLoader(ItemLoader):
    default_input_processor = MapCompose(unicode.strip, filter_line_diagonal)
    default_output_processor = TakeFirst()

    advantage_in = MapCompose(unicode.strip)
    advantage_out = Join()

    description_in = MapCompose(unicode.strip)
    description_out = Join()

    address_in = MapCompose(unicode.strip, filter_line_combine)

    category_in = Identity()
    category_out = TakeFirst()


# noinspection PyMethodMayBeStatic
class LagouSpider(DSpider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = (
        'https://www.lagou.com/',
    )

    rules = (
        # Rule(LinkExtractor(allow="/jobs/[0-9]+\.html"), callback='parse_1', follow=False),
        Rule(LinkExtractor(allow="/zhaopin/.*/.*"), callback='parse_0', follow=True),
    )

    def parse_0(self, response):
        url = response.request.url
        category = url.split("/")[4].decode('unicode-escape')
        child_urls = response.xpath('//a[contains(@class, "position_link")]/@href').re(r'/jobs/[0-9]+\.html')
        # logging.debug(child_urls)
        for child_url in child_urls:
            yield Request("https://" + "www.lagou.com" + child_url, meta={'category': category}, callback=self.parse_1)

    def parse_1(self, response):
        category = response.meta['category']
        lagou_loader = LagouLoader(item=LagouItem(), response=response)
        # referer = response.request.headers.get('Referer', None) ## 如何从response 中获取请求的一些信息
        lagou_loader.add_xpath('title',
                               "//div[contains(@class, 'ceil')]/span[contains(@class,'ceil-job')]/text()")
        lagou_loader.add_xpath('lagou_id', "//input[@id='jobid']/@value")
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
        lagou_loader.add_xpath('district', "//div[contains(@class, 'work_addr')]/a[2]/text()")
        lagou_loader.add_xpath('description', "//dd[contains(@class, 'job_bt')]/div//text()")
        lagou_loader.add_xpath('cpn_name', "//dl[contains(@class, 'job_company')]//h2[contains(@class, 'fl')]/text()")
        lagou_loader.add_xpath('cpn_finance_round',
                               "//dl[contains(@class, 'job_company')]//ul[contains(@class, 'c_feature')]/li[2]/text()")
        lagou_loader.add_xpath('cpn_scale',
                               "//dl[contains(@class, 'job_company')]//ul[contains(@class, 'c_feature')]/li[3]/text()")
        lagou_loader.add_xpath('cpn_field',
                               "//dl[contains(@class, 'job_company')]//ul[contains(@class, 'c_feature')]/li[1]/text()")
        lagou_loader.add_xpath('cpn_web_page',
                               "//dl[contains(@class, 'job_company')]//ul[contains(@class, 'c_feature')]/li[4]/a/text()")
        lagou_loader.add_xpath('biz_area', "//div[contains(@class, 'work_addr')]/a[3]/text()")
        lagou_loader.add_xpath('address', "//div[contains(@class, 'work_addr')]/text()")
        lagou_loader.add_value('category', category)
        return lagou_loader.load_item()

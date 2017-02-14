# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = (
        # 'https://www.lagou.com/',
        'https://www.lagou.com/zhaopin/duomeitishejishi/',
    )

    def parse(self, response):
        self.parse_boot(response=response)
        # self.parse_item(response=response)

    def parse_boot(self, response):
        urls = []
        for sel in response.xpath("//div[contains(@class, 'menu_box')]//a"):
            url = sel.xpath("@href").extract()[0]
            # text = sel.xpath("text()").extract()[0]
            urls.append(url)

        for url in urls:
            request = scrapy.Request("https://" + url, callback=self.parse_item)
            yield request

    def parse_item(self, response):
        urls = []
        for sel in response.xpath("//div[contains(@class, 's_position_list')]//a[contains(@class, 'position_link')]"):
            url = sel.xpath("@href").extract()[0]
            print url
            urls.append(url)

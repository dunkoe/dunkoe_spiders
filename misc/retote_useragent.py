# -*-coding:utf-8-*-

# noinspection PyByteLiteral
"""
避免被ban策略之一：使用useragent池。
使用注意：需在settings.py中进行相应的设置。
"""

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from agents import AGENTS_ALL


# noinspection PyByteLiteral
class RotateUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent=''):
        super(RotateUserAgentMiddleware, self).__init__(user_agent)
        self.user_agent = user_agent

    def process_request(self, request, spider):
        """
        模拟ua
        :param request:
        :param spider:
        :return:
        """
        ua = random.choice(AGENTS_ALL)
        if ua:
            import logging
            logging.debug("******** Current UserAgent :%s" % ua)
            request.headers.setdefault('User-Agent', ua)

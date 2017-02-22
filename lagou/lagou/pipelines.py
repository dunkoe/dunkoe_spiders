# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# noinspection PyMethodMayBeStatic
import json
import time


# noinspection PyMethodMayBeStatic
class LagouPipeline(object):

    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    """
        将爬虫到的对象以json格式存储到文件中
        """

    def __init__(self):
        format_time = time.strftime("%Y%m%d", time.localtime(int(time.time())))
        file_name = "lagou." + format_time + ".json"
        self.file = open(file_name, 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class MySQLWriterPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        pass

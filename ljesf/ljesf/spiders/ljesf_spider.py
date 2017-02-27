# -*- coding: utf-8 -*-
import scrapy


class LjesfSpiderSpider(scrapy.Spider):
    name = "ljesf_spider"
    allowed_domains = ["lianjia.com"]
    start_urls = (
        'http://bj.lianjia.com/ershoufang/',  # 北京

        # 'http://cd.lianjia.com/ershoufang/',  # 成都
        # 'http://cq.lianjia.com/ershoufang/',  # 重庆
        # 'http://cs.lianjia.com/ershoufang/',  # 长沙
        #
        # 'http://dl.lianjia.com/ershoufang/',  # 大连
        # 'http://dg.lianjia.com/ershoufang/',  # 东莞
        #
        # 'http://fs.lianjia.com/ershoufang/',  # 佛山
        #
        # 'http://gz.lianjia.com/ershoufang/',  # 广州
        #
        # 'http://hz.lianjia.com/ershoufang/',  # 杭州
        # 'http://hk.lianjia.com/ershoufang/',  # 海口
        # 'http://hf.lianjia.com/ershoufang/',  # 合肥
        #
        # 'http://jn.lianjia.com/ershoufang/',  # 济南
        #
        # 'http://ls.lianjia.com/ershoufang/',  # 陵水
        # 'http://lf.lianjia.com/ershoufang/',  # 廊坊
        #
        # 'http://nj.lianjia.com/ershoufang/',  # 南京
        #
        # 'http://qd.lianjia.com/ershoufang/',  # 青岛
        # 'http://qh.lianjia.com/ershoufang/',  # 琼海
        #
        # 'http://sh.lianjia.com/ershoufang/',  # 上海
        # 'http://sz.lianjia.com/ershoufang/',  # 深圳
        # 'http://su.lianjia.com/ershoufang/',  # 苏州
        # 'http://sjz.lianjia.com/ershoufang/',  # 石家庄
        # 'http://sy.lianjia.com/ershoufang/',  # 沈阳
        # 'http://san.lianjia.com/ershoufang/',  # 三亚
        #
        # 'http://tj.lianjia.com/ershoufang/',  # 天津
        #
        # 'http://wh.lianjia.com/ershoufang/',  # 武汉
        # 'http://wc.lianjia.com/ershoufang/',  # 文昌
        # 'http://wn.lianjia.com/ershoufang/',  # 万宁
        #
        # 'http://xm.lianjia.com/ershoufang/',  # 厦门
        # 'http://xa.lianjia.com/ershoufang/',  # 西安
        #
        # 'http://yt.lianjia.com/ershoufang/',  # 烟台
        #
        # 'http://zs.lianjia.com/ershoufang/',  # 中山
        # 'http://zh.lianjia.com/ershoufang/',  # 珠海
    )

    def parse(self, response):
        pass

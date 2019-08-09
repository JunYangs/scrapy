# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    caseName = scrapy.Field()  # 案件名称
    name = scrapy.Field()  # 被处罚对象
    documentNo = scrapy.Field()  # 行政处罚决定书文号
    date = scrapy.Field()  # 处罚日期
    detailUrl = scrapy.Field()  # 详细内容url


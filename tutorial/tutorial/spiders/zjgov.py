#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
************************
 Written by : QiuJunYang
 Date: 08/08/2019
************************
'''

import re
import scrapy
from tutorial.items import TutorialItem


class ZjGov(scrapy.Spider):
    name = "zjGov"
    allowed_domains = ['zjzwfw.gov.cn']  # 爬取范围
    start_urls = [
         'http://www.zjzwfw.gov.cn/zjzw/punish/frontpunish/searchall_list.do?areacode=330101&xzcf_code=&pageNo=1'
    ]

    # 页码处理
    def parseOther(self, response):
        pageNum = response.xpath('//*[@id="xzcf_1"]/div/ul/li[6]/text()').extract()[0]
        pageNum = re.compile(r'\d+').findall(pageNum)[0]  # 总页数
        # Url拆分合并
        urlSplit = self.start_urls[0].split('=', 3)  # 下一页
        urlNext = urlSplit[0] + '=' + urlSplit[1] + '=' + urlSplit[2] + '='
        list = [pageNum, urlNext]
        return list

    # 页面解析
    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parseNext)  # 第一页
        # pageNum = self.parseOther(response)[0]
        # urlNext = self.parseOther(response)[1]
        flag = True
        while flag:
            for i in range(2, int(self.parseOther(response)[0])+1):
                yield scrapy.Request(self.parseOther(response)[1]+str(i), callback=self.parseNext)
            flag = False

    # 页面信息处理
    def parseNext(self, response):
        for i in response.xpath('//*[@id="xzcf_1"]/table'):
            item = TutorialItem()
            item['caseName'] = i.xpath('tr/td[1]/a/text()').extract()[0]   # 案件名称
            item['name'] = i.xpath('tr/td[2]/text()').extract()[0]   # 被处罚对象
            item['documentNo'] = i.xpath('tr/td[3]/text()').extract()[0]  # 行政处罚决定书文号
            item['date'] = i.xpath('tr/td[4]/text()').extract()[0]  # 处罚日期
            item['detailUrl'] = i.xpath('tr/td[1]/a/@href').extract()[0]  # 详细内容url
            yield item

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
import requests
from lxml import etree
import tutorial.ISConstant
from tutorial.items import TutorialItem


class ZjGov(scrapy.Spider):
    name = "zjGov"
    allowed_domains = ['zjzwfw.gov.cn']  # 爬取范围
    start_urls = [
         'http://www.zjzwfw.gov.cn/zjzw/punish/frontpunish/searchall_list.do?areacode=330101&xzcf_code=&pageNo=1'
    ]

    # URL拼接
    def parseOther(self, response, cityUrl):
        pageNum = response.xpath('//*[@id="xzcf_1"]/div/ul/li[6]/text()').extract()[0]
        pageNum = re.compile(r'\d+').findall(pageNum)[0]  # 总页数
        # Url拆分合并
        urlSplit = cityUrl.split('=', 3)  # 拆分
        urlNext = urlSplit[0] + '=' + urlSplit[1] + '=' + urlSplit[2] + '='  # 合并
        list = [pageNum, urlNext]
        return list

    # 页面获取
    def parse(self, response):
        for cityUrl in list(tutorial.ISConstant.cityUrl.values()):  # ISConstant.py常量
            yield scrapy.Request(cityUrl, callback=self.parseNext)  # 第一页
            pageNum = self.parseOther(response, cityUrl)[0]  # 总页数
            urlNext = self.parseOther(response, cityUrl)[1]  # 下一页
            for i in range(2, int(pageNum)+1):
                yield scrapy.Request(urlNext+str(i), callback=self.parseNext)

    # 页面解析
    def parseNext(self, response):
        urlHead = tutorial.ISConstant.SITEURL
        for i in response.xpath('//*[@id="xzcf_1"]/table'):
            item = TutorialItem()
            item['caseName'] = i.xpath('tr/td[1]/a/text()').extract()[0]   # 案件名称
            item['name'] = i.xpath('tr/td[2]/text()').extract()[0]   # 被处罚对象
            item['documentNo'] = i.xpath('tr/td[3]/text()').extract()[0]  # 行政处罚决定书文号
            item['date'] = i.xpath('tr/td[4]/text()').extract()[0]  # 处罚日期
            urltail = i.xpath('tr/td[1]/a/@href').extract()[0]  # 行政处罚详细内容URL
            item['detail'] = self.parseContent(urlHead+urltail)  # 行政处罚详细内容
            yield item

    # 行政处罚详细内容
    def parseContent(self, url):
        res = requests.get(url, headers=tutorial.ISConstant.HEADERS).text
        html = etree.HTML(res)
        content = html.xpath('/html/body/table[3]/tr/td/table/tr/td/table[5]/tr/td/p/text()')
        return content

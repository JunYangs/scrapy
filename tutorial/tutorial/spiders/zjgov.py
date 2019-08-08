#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
#########################
 Written by : QiuJunYang
 Date: 08/08/2019
#########################
'''

import scrapy


class ZjGov(scrapy.Spider):
    name = "zjGov"
    allowed_domains = ['zjzwfw.gov.cn']  # 爬取范围
    start_urls = [
         'http://www.zjzwfw.gov.cn/zjzw/punish/frontpunish/searchall_list.do?areacode=330101&xzcf_code=&pageNo=1'
    ]

    # def start_requests(self):  # start_urls=[] 第二种写法
    #     urls = [
    #         'http://www.zjzwfw.gov.cn/zjzw/punish/frontpunish/searchall_list.do?areacode=330101&xzcf_code=&pageNo=1'
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.parseNext)  # 第一页
        pageNum = response.xpath('//*[@id="xzcf_1"]/div/ul/li[6]').extract()[0]

        urlSplit = self.start_urls[0].split('=', 3)  # 其它页
        urlNext = urlSplit[0]+'='+urlSplit[1]+'='+urlSplit[2]+'='
        for i in range(0, pageNum):
            yield scrapy.Request(urlNext+'%d' % i, callback=self.parseNext)
        # for page in response.xpath('//*[@id="xzcf_1"]/div/ul/li[6]'):  # 其它页
        #     urlNext = page.xpath('').extract()[0]
        #     yield scrapy.Request(urlNext, callback=self.parseNext)

    def parseNext(self, response):
        pass
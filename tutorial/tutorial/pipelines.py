# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TutorialPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect("localhost", "root", "root", "")

    def process_item(self, item, spider):
        return item

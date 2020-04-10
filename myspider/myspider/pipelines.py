# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    #process_item方法名是固定的写法
    def process_item(self, item, spider):
        print(item)
        if item["web_name"]=="jd":
            pass

        return item
class MyspiderPipeline2(object):
    #process_item方法名是固定的写法
    def process_item(self, item, spider):# spider是爬虫的类名
        #获取爬虫的名称
        name = spider.name #itcast
        print(item)

        return item

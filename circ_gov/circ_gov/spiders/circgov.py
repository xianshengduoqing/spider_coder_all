# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from time import sleep

"""
新知识 CrawlSpider
 
    Rule(LinkExtractor(allow=r'http://bxjg.circ.gov.cn/web/site0/tab5207/info4103964.htm'), callback='parse_item', follow=True),
    allow:正则范围的地址
    callback:对allow地址的内容 通过callback 指定函数去解析
    follow:  True:表示 爬虫会从start_urls地址的页面中去寻找指定符合的url 作为start_url,(我的理解就是很多个房屋大门的钥匙，callback相当于门内各个物件的钥匙，)
    
    注意一定要打开User_agen设置

"""
class CircgovSpider(CrawlSpider):
    name = 'circgov'
    allowed_domains = ['circ.gov.cn']
    # start_urls = ['http://bxjg.circ.gov.cn/']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5207/module14337/page1.htm']

    rules = (

        Rule(LinkExtractor(allow=r'/web/site0/tab5207/info\d+\.htm'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'http://bxjg.circ.gov.cn/web/site0/tab5207/module14337/page\d+\.htm'), follow=True),
    )

    def parse_item(self, response):
        print("====================================================================")
        item = {}
        sleep(5)
        item["title"]=response.xpath("//table[@id='tab_content']/tbody/tr[1]/td//text()").extract()
        print(item["title"])

        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

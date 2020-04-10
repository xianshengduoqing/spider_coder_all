# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' # 爬虫名
    allowed_domains = ['itcast.cn']#允许爬取的域名
    # start_urls = ['http://itcast.cn/']#要爬取的地址
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#ajavaee"]

    def parse(self, response):
        #爬取itscast师资库
        # result = response.xpath("//div[@class='graybg tea_main']//h3/text()")
        # result = response.xpath("//div[@class='graybg tea_main']//h3/text()").extract() #extract 会抽取所有字符串
        #print(result)
        #分组获取
        li_list = response.xpath("//div[@class='graybg tea_main']//li")
        for li in li_list:
            item={}
            item["web_name"]= "jd"
            item["name"] = li.xpath(".//h3/text()").extract_first() #extract_first()  获取第一个字符串，没有显示None
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            yield  item  #这里的item 只能是requests对象、BaseItem、dict None类型
        pass

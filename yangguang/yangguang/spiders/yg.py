# -*- coding: utf-8 -*-
import scrapy
import re
from yangguang.items import YangguangItem
class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest']

    def parse(self, response):
        """
        item 翻页爬取
        爬取阳光热线问政最新问政，时间，问题，状态，问题内容
        :param response:
        :return:
        """
        #"分组"
        li_list = response.xpath("//ul[@class='title-state-ul']/li")
        print(li_list)
        for li in li_list:
            item = YangguangItem()
            item['question_time'] = li.xpath("./span[@class='state5 ']/text()").extract_first()
            item['title'] = li.xpath("./span[@class='state3']/a/text()").extract_first()
            item['status'] = re.sub(r"\n\s+","",li.xpath("./span[@class='state2']/text()").extract_first())
            title_url = 'http://wz.sun0769.com/'+li.xpath("./span[@class='state3']/a/@href").extract_first()
            meta = {"item":item}
            yield  scrapy.Request(title_url, callback=self.parse_content,meta=meta)
        """分页"""
        next_url = response.xpath("//div[@class='mr-three paging-box']/a[@class='arrow-page prov_rota']/@href").extract_first()
        if next_url !=None:
            print("******************************下一页************************************************************")
            url = "http://wz.sun0769.com/"+next_url
            yield scrapy.Request(url=url,callback=self.parse)
        pass
    def parse_content(self,response):
        item = response.meta["item"]
        # content=response.xpath("//p[@class='focus-details']/text()").extract_first()
        item['content'] = response.xpath("//div[@class='details-box']/pre/text()").extract()
        print(item)
        # yield item

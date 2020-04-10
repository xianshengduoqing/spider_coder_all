# -*- coding: utf-8 -*-
import scrapy


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tieba.baidu.com']
    # start_urls = ['http://hr.tencent.com/']
    start_urls = ['https://tieba.baidu.com/p/6606283520']

    def parse(self, response):
        li_list = response.xpath("//div[@class='p_postlist']//div[@class='l_post l_post_bright j_l_post clearfix  ']")
        print(li_list)
        for li in li_list:
            item={}
            item['position'] = li.xpath(".//div[@class='d_post_content j_d_post_content ']/text()").extract_first()
            print(item)
        #实现翻页功能
        page_list = response.xpath("//li[@class='l_pager pager_theme_5 pb_list_pager']//a")
        next_page = None
        for page in page_list:
            text = page.xpath("./text()").extract_first()
            if text=="下一页":
                next_page=page
        if next_page != None:
            print("===================================================================================")
            next_url = "https://tieba.baidu.com/"+next_page.xpath("./@href").extract_first()#获取元素的属性
            yield scrapy.Request(next_url,callback=self.parse)#注意不带括号

        # print(page_list)
        pass


"""
知识点
scrapy pipline 返回请求对象
scrapy.Request(next_url,callback=self.parse)#注意不带括号
详细参数：
scrapy.Reques(url, callback=None, method='GET', headers=None, body=None,
             cookies=None, meta=None, encoding='utf-8', priority=0,
             dont_filter=False, errback=None, flags=None)
1、callbach:处理url的解析函数
2、method:请求方法，如果是POST,则需要传body
3、cookies 不能放入headers中
4、meta:用于解析函数传递参数，是字典格式
    设置
    def parse(self,response):
        meta = {"item":item}
        yield scrapy.Request(url,self.parse2,meta=meta)
    获取
    def parse2(self,response)：
         #获取parse的meta 中的item
         item = response.meta["item"]

元素的属性获取
+next_page.xpath("./@href").extract_first()
"""
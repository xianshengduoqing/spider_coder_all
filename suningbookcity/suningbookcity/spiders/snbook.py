# -*- coding: utf-8 -*-
import scrapy
import re
from copy import deepcopy
"""
爬取苏宁 图书的 所有分类的图书 的大分类、小分类、书名 、作者、图书的价格

"""


class SnbookSpider(scrapy.Spider):
    name = 'snbook'
    allowed_domains = ['suning.com']
    # start_urls = ['http://book.suning.com/']
    start_urls = ['https://book.suning.com/?safp=d488778a.10038.0.8cca61ce53&safpn=10006.502320']

    def parse(self, response):
        div_list = response.xpath("//div[@class='menu-list']//div[@class='menu-item']")
        #分组查询
        for div in div_list:
            big_class = div.xpath("./dl/dt/h3/a/text()").extract_first()
            item = {}
            mid_a_list = div.xpath("./dl/dd/a")
            for a in mid_a_list:

                mid_url = a.xpath("./@href").extract_first()
                mid_class = a.xpath("./text()").extract_first()
                item["big_class"] = big_class
                item["mid_class"] = mid_class
                item["mid_url"] = mid_url
                yield scrapy.Request(url=item["mid_url"], callback=self.parse_mid_class, meta={"item": deepcopy(item)})


    #翻页查询
    #获取最后一个td
    # response.xpath(//td[last()])
    # response.xpath(//td[2])
    #//a[text()='<']/@href
    def parse_mid_class(self, response):
        item = deepcopy(response.meta["item"])
        # item = response.meta["item"]
        # mid_class = item.get("mid_class")

        # print(mid_class)
        book_list = response.xpath("//ul[@class='clearfix']//li")
        # print("==========================",book_list)
        for book in book_list:
            book_url = "https:"+book.xpath("./div[@class='border-out']//div[@class='img-block']//a/@href").extract_first()
            item["boo_url"]=book_url
            yield scrapy.Request(
                url=book_url,
                callback=self.parse_book_price_name,
                meta={"item":deepcopy(item)})
        #/1-502320-0-0-0-0-0-0-0-4.html  页码规律
        #翻页实现
        #翻页ajax
        # param.currentPage = "3";
        #param.pageNumbers = "100";
        print(item['mid_class'])
        aa = re.findall('param.currentPage = "(.*?)";', response.body.decode())[0]
        cur_page = re.findall('param.currentPage = "(.*?)";',response.body.decode())[0]
        pageNumbers = re.findall('param.pageNumbers = "(.*?)";',response.body.decode())[0]
        pageNumbers = int(pageNumbers.strip())
        cur_page = int(cur_page.strip())
        categoryId = re.findall('"categoryId": "(.*?)"',response.body.decode())[0]
        if cur_page<pageNumbers:
            next_url ="https://list.suning.com"+"/1-"+categoryId+"-" + str(cur_page+1) + "-0-0-0-0-0-0-4.html"
            yield scrapy.Request(url=next_url,callback=self.parse_mid_class,meta={"item":item})



    def parse_book_price_name(self, response):
        item = response.meta["item"]

        # item["bk_name"] = [re.sub(r"\r+|\t+|\n+|\s+", "", i) for i in response
        item["bk_name"] = [re.sub(r"\s",'',i)for i in response
            .xpath("//div[@class='proinfo-main']//div[@class='proinfo-title']/h1/text()").extract()]
        # print(bk_name)
        # bk_price = response.xpath("//div[@class='proinfo-main']//div[@class='proinfo-focus clearfix']//dl[@class='price-promo']")
        # print("==================",bk_price)
        print(item)
"""
几点注意事项
from copy import deepcopy
1、爬虫 经过多次连接并且是异步请求 scrap.Restquest(),原有的item被覆盖，需要deepcopy(item)拷贝防止覆盖
2、div 中没有连接地址，通过ajax请求，需要从全文中匹配相关参数 re.findall("（.*?）",response.body.decode())[0]
3、小知识总结
   xpath : 
    越级查找 //  //div[@class='aaa']//a  任意子a
    下级查找 /  //div[@class='aaa']/a   儿子被a
     获取属性  //div[@class='aaa']//a/@href
     获取属性  //div[@class='aaa']//a/@src
     获取属性  //div[@class='aaa']//a/@art
    符合元素的最后一个 last() //div[last()]
    符合元素的一个 last() //div[0]
    reponse全文：response.body.decode()
    re 正则：
    正则替换  re.sub("re","",string) ，将string 中符合正则的替换为空
    正则查找  re.findall("re",string)
    拷贝： deecopy
    scrapy:
    meta 传递数据 ：scrapy.Request(url=next_url,callback=self.parse_mid_class,meta={"item":item})
    settings 必须有USER_AGENT配置，不然一眼就能看出是爬虫
    
    


"""



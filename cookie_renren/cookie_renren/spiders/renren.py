# -*- coding: utf-8 -*-
import scrapy
import re

"""
需要用携带cookie 抓取信息


1、cookie设置在 def start_requests里设置
2、由start_request 发起request请求 parse解析函数
3、cookie必须是字典形式

"""


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/9742/profile']

    def start_requests(self):
        cookies="anonymid=jx4twlzcuwgug6; _r01_=1; depovince=GW; taihe_bi_sdk_uid=315e9d55d5136c62e13cb87220a3829d; JSESSIONID=abcylWWP9EcHC9y52CWfx; ick_login=eea3a643-7bcb-4d6a-b786-211627dad251; taihe_bi_sdk_session=ef84b8dbea69563ef9c497ae0149e39a; ick=b018b535-58cb-458c-aa7d-f867f52991f3; jebe_key=8f68e5e7-8bac-45fe-a5da-2c3964fe88c0%7Cab5db306a5cf772c8940e9e5ef4ea11b%7C1586729709494%7C1%7C1586729709063; wp_fold=0; XNESSESSIONID=1a767befec83; jebecookies=350ab80b-3937-4751-81d7-f7b9210f1e8d|||||; _de=64B796360B44323CEA4DAC6267064EB2; p=bf71d1704988a56d630a1a3403eee7b18; first_login_flag=1; ln_uact=13651229936; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=8e59930357d45af752f7324ebb2bf30d8; societyguester=8e59930357d45af752f7324ebb2bf30d8; id=974217438; xnsid=8f7f700d; ver=7.0; loginfrom=null"
        cookies = {cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )
        pass

    def parse(self, response):
        name = re.findall("新用户29936", response.body.decode())
        print(name)

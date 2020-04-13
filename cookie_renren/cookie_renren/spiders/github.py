# -*- coding: utf-8 -*-
import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"login":"957208964@qq.com","password":"XXXXX"},
            callback=self.after_login
        )
    def after_login(self,response):
        print("=================")
        print(response)
        print(re.findall("spider_coder_all",response.body.decode()))
    #=================================================================
    # def parse(self, response):
    #     authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
    #     ga_id = response.xpath("//input[@name='ga_id']/@value").extract_first()
    #     login="957208964@qq.com"
    #     password="XXXXXXXX"
    #     commit=response.xpath("//input[@name='commit']/@value").extract_first()
    #     timestamp=response.xpath("//input[@name='timestamp']/@value").extract_first()
    #     timestamp_secret=response.xpath("//input[@name='timestamp_secret']/@value").extract_first()
    #     # webauthn-support=response.xpath("//input[@name='webauthn-support']/@value").extract_first()
    #     # webauthn-iuvpaa-support=response.xpath("//input[@name='webauthn-iuvpaa-support']/@value").extract_first()
    #     formdata=dict(authenticity_token=authenticity_token,
    #                   login=login,
    #                   password=str(password),
    #                   commit=commit,
    #                   timestamp=timestamp,
    #                   timestamp_secret=timestamp_secret,
    #
    #                   )
    #     print(formdata)
    #
    #     yield scrapy.FormRequest(
    #         "https://github.com/session",
    #         formdata=formdata,
    #         callback=self.after_login
    #     )
    # def after_login(self,response):
    #     print("=================")
    #     print(response)
    #     print(re.findall("spider_coder_all",response.body.decode()))




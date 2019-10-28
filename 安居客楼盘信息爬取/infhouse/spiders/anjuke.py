# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import InfhouseItem

class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    # start_urls = ['http://anjuke.com/']
    def __init__(self,local='hf', *args,**kwargs):
        super(AnjukeSpider, self).__init__(*args,**kwargs)
        self.local=local
        url=f'https://{local}.fang.anjuke.com/loupan/all/'
        self.start_urls=[url]

    def parse(self, response):
        data=response.xpath('//div[@class="key-list imglazyload"]/div[contains(@data-soj,"AF_RANK")]')
        for li in data:
            deturl=li.xpath('.//a[contains(@soj,"AF_RANK")]/@href').get()
            yield scrapy.Request(url=deturl,callback=self.parse1)
        if response.xpath('//div[@class="pagination"]/a[@class="next-page next-link"]'):
            npage=response.xpath('//div[@class="pagination"]/a[@class="next-page next-link"]/@href').get()
            yield scrapy.Request(url=npage,callback=self.parse)

    def parse1(self,response):
        item=InfhouseItem()
        item['name']=response.xpath('//div[@class="basic-details"]//div[@class="basic-info"]/h1/text()').get()
        try:
            item['price']=response.xpath('//em[@class="sp-price other-price"]/text()').get()
        except:
            item['price']='待定'
        item['starttime']=response.xpath('//dl[@class="basic-parms clearfix"]/dd[2]/span/text()').get()
        item['opentime']=response.xpath('//dl[@class="basic-parms clearfix"]/dd[3]/span/text()').get()
        housetypes=response.xpath('//div[@class="house-item g-overflow"]/a/text()').getall()
        item['housetype']=' '.join(housetypes)
        item['localtion']=response.xpath('//dd[@class="last-line g-overflow"]/a[@class="lpAddr-text g-overflow"]/text()').get().strip()
        yield item
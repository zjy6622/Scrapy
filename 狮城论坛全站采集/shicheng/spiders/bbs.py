# -*- coding: utf-8 -*-
import scrapy
from aip import AipOcr
from ..items import ShichengItem
import re

class  BbsSpider (scrapy.Spider):
    name = 'bbs'
    allowed_domains = ['bbs.sgcn.com']
    start_urls = ['http://bbs.sgcn.com/forum.php?gid=1163']
    APP_ID = '17369136'
    API_KEY = '9YGvGo89eiSenFODTIKMvWCP'
    SECRET_KEY = 'Fu7TnMM0ZTeC2LjkfXwLx9537Kwk8F2B'

    def __init__(self,num,*args,**kwargs):
        super().__init__(*args,**kwargs)
        APP_ID = '17369136'
        API_KEY = '9YGvGo89eiSenFODTIKMvWCP'
        SECRET_KEY = 'Fu7TnMM0ZTeC2LjkfXwLx9537Kwk8F2B'
        self.num=num
        self.typelist = {}
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        self.nums = getattr(self, 'num')

    def parse (self, response):
        tr=response.xpath('//table[@class="fl_tb"]//tr')                                                 #从广告主页面提取各个分类广告的url，并放入字典，使其一一对应
        for td in tr:
            url=td.xpath('./td/h2/a/@href').get()
            name=td.xpath('./td/h2/a/text()').get()
            self.typelist[name]=url
        if self.nums == '房产信息'or self.nums == '房间出租':                                            #房产信息和房屋出租的内部还有分类，判断出后特别处理
            urls = self.typelist[self.nums]
            yield scrapy.Request(url=urls,callback=self.roomparse)
        elif self.nums == '服装配饰'or self.nums == '美容美发' or self.num == '鞋帽箱包':                #这3个详情页由图片加载，判断出后特别处理
            urls = self.typelist[self.nums]
            yield scrapy.Request(url=urls, callback=self.tpparse)
        else:
            urls=self.typelist[self.nums]                                                                #从字典中查找对应的url
            yield scrapy.Request(url=urls,callback=self.parse1)

    def parse1(self,response):
        tbody=response.xpath('//tbody[contains(@id,"normalthread")]')
        for td in tbody:
            url=td.xpath('.//td[@class="icn"]/a/@href').get()
            yield scrapy.Request(url=url,callback=self.parse2)
        if response.xpath('//span[@id="fd_page_bottom"]//a[@class="nxt"]/@href'):                               #翻页
            nexturl=response.xpath('//span[@id="fd_page_bottom"]//a[@class="nxt"]/@href').get()
            print(nexturl)
            yield scrapy.Request(url=nexturl,callback=self.parse1)

    def parse2 (self, response):#详情页提取
        item=ShichengItem()
        if response.xpath('//table[@class="cgtl mbm"]//th[contains(text(),"电话:")]//following::*[1]/img'):     #判断是否是图片，如果是提交百度云识别
            phonepng=response.xpath('//table[@class="cgtl mbm"]//th[contains(text(),"电话:")]//following::*[1]/img/@src').get()
            phoneurl=phonepng.replace('./','https://bbs.sgcn.com/')
            baiduai= self.client.basicGeneralUrl(phoneurl)                                                      #百度识别返回图片中的电话号码
            phone=baiduai['words_result'][0]['words']
            item['phone']=phone
            item['warning'] = '*'
        elif response.xpath('//table[@class="cgtl mbm"]//th[contains(text(),"电话:")]//following::*[1]/text()'): #判断如果不是图片，直接提取内容
            item['phone']=response.xpath('//table[@class="cgtl mbm"]//th[contains(text(),"电话:")]//following::*[1]/text()').get()
            item['warning'] = '*'
        else:
            item['phone'] = '无'
            item['warning']='非广告内容，无法提取'
        content=response.xpath('//table[@class="cgtl mbm"]//tr[1]/td/text()').get('无')
        item['content']=self.chinese(content)
        item['name']=response.xpath('//table[@class="cgtl mbm"]//tr[3]/td/text()').get('无')
        item['wechat']=response.xpath('//table[@class="cgtl mbm"]//th[contains(text(),"微信:")]/following::*[1]/text()').get('无')
        if response.xpath('//div[contains(@id,"post_")][1]//td[@class="t_f"]//font'):                           #由于不同详情页的内容xpath提取的方法不同，不得不写这么多判断
            data = response.xpath('//div[contains(@id,"post_")][1]//td[@class="t_f"]//font/text()').getall()
            # print(data)
            item['contents'] = ''.join(data).replace('\r\n', '').strip()
        else:
            response.xpath('//div[contains(@id,"post_")][1]//td[@class="t_f"]/text()')
            data=response.xpath('//div[contains(@id,"post_")][1]//td[@class="t_f"]/text()').getall()
            item['contents'] = ''.join(data).replace('\r\n', '').strip()
        yield item

    def roomparse(self,response):                                                                               #房产信息和房屋出租的处理方法，进一步提取url
        tbody=response.xpath('//table[@class="fl_tb"]//tr')
        for tr in tbody:
            url=tr.xpath('./td/h2/a/@href').get(False)
            if url:
                yield scrapy.Request(url=url,callback=self.parse1)

    def tpparse(self,response):
                                                                                                   #'服装配饰','美容美发','鞋帽箱包'的详情页提取url
        ul=response.xpath('//ul[@id="waterfall"]/li')
        for li in ul:
            url=li.xpath('.//h3/a/@href').get()
            yield scrapy.Request(url=url, callback=self.parse2)
        if response.xpath('//span[@id="fd_page_top"]//a[@class="nxt"]'):
            nexturl=response.xpath('//span[@id="fd_page_top"]//a[@class="nxt"]/@href').get()
            yield scrapy.Request(url=nexturl,callback=self.tpparse)

    @staticmethod                                                                                   #提取字符串中的中文字符
    def chinese(txt):
        pattern = re.compile("[\u4e00-\u9fa5]")
        return "".join(pattern.findall(txt))
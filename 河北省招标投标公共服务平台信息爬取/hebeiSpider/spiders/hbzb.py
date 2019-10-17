# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from ..items import HebeispiderItem
import re
import copy

class HbzbSpider(scrapy.Spider):
    name = 'hbzb'
    allowed_domains = ['hebeieb.com']
    # start_urls = ['http://www.hebeieb.com/tender/xxgk/list.do?selectype=zbgg#']


    def start_requests(self):      #因为是post请求，而scrapy默认为get请求，需要重写父类方法start_requests
        url='http://www.hebeieb.com/tender/xxgk/zbgg.do'
        for num in range(0,3):
            form_data={
                'page': str(num),
                'TimeStr':'',
                'allDq': 'reset2',
                'allHy': 'reset1',
                'AllPtName':'',
                'KeyStr':'',
                'KeyType': 'ggname'
            }
            request=FormRequest(url=url,formdata=form_data,callback=self.parse)
            yield request

    def parse(self, response):
        item=HebeispiderItem()
        data=response.xpath('//div[@class="publicont"]')
        for dat in data:
            href='http://www.hebeieb.com'+re.sub('detail','newDetail',dat.xpath('.//h4/a/@href').get())
            item['title']=dat.xpath('.//h4/a/@title').get()
            print(dat.xpath('.//h4/a/@title').get())
            item['city']=dat.xpath('.//p[@class="p_tw"]/span[@class="span_on"][1]/text()').get()
            item['inmfrom']=dat.xpath('.//p[@class="p_tw"]/span[@class="span_on"][2]/text()').get()
            item['inmtype']=dat.xpath('.//p[@class="p_tw"]/span[@class="span_on"][3]/text()').get()
            item['industry']=dat.xpath('.//p[@class="p_tw"]/span[@class="span_on"][4]/text()').get()
            yield FormRequest(url=href,meta={'item':copy.deepcopy(item) },callback=self.parse1) #将这次相应中的有用信息加入meta中，在下面解析后一起传给管道文件（要注意：由于meta是浅拷贝，在for循环后值会被改变，在这改为深拷贝）
    def parse1(self,response):
        item = response.meta['item']
        texts=response.xpath('//p[@class="MsoListParagraph"]//text()').getall()
        ts=[]
        for t in texts:
            s = re.sub('\s', '', t)
            if s != '':
                ts.append(s)
        item['text']=''.join(ts).strip()
        phone=response.xpath('//table/tbody//text()').getall()
        ps=[]
        for p in phone:
            s=re.sub('\s', '', p)
            if s !='':
                ps.append(s)
        item['phones']='  '.join(ps)
        yield item







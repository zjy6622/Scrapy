# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import ZihuItem
import re

class ZhihuSpider(scrapy.Spider):
    name = 'zhiHU'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v4/members/WaJueJiPrince/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20']
    idlist = []
    def parse(self, response):
        data=json.loads(response.text)
        if data.get('data',False):
            item=ZihuItem()
            nowurl=response.body_as_unicode()
            for jsondata in data.get('data'):
                # print(jsondata)
                item['name']=jsondata.get('name')
                item['content']=jsondata.get('headline')
                item['jpg']=jsondata.get('avatar_url')
                item['froms'] =re.search('members/(.*?)/followers',nowurl).group(1)
                id=jsondata.get('url_token')
                self.idlist.append(id)
                yield item
        if data.get('paging',False):
            if not data['paging']['is_end'] and data['paging']['next']:
                nextpage=data['paging']['next']
                next_url=nextpage.replace('members','api/v4/members')
                yield scrapy.Request(url=next_url,callback=self.parse)
            else:
                url='https://www.zhihu.com/api/v4/members/ponyma/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
                for i in self.idlist:
                    i=re.sub('ponyma',i,url)
                    yield scrapy.Request(url=i,callback=self.parse)




# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShichengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    phone=scrapy.Field()
    content=scrapy.Field()
    name=scrapy.Field()
    wechat=scrapy.Field()
    warning=scrapy.Field()
    contents=scrapy.Field()


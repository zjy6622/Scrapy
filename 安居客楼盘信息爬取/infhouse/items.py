# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InfhouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    starttime = scrapy.Field()
    opentime = scrapy.Field()
    housetype = scrapy.Field()
    localtion = scrapy.Field()


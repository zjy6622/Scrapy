# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HebeispiderItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    href = scrapy.Field()
    inmfrom = scrapy.Field()
    inmtype = scrapy.Field()
    industry = scrapy.Field()
    text = scrapy.Field()
    phones = scrapy.Field()
    title = scrapy.Field()


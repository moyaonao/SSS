# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    position = scrapy.Field()
    company = scrapy.Field()
    pay = scrapy.Field()
    area = scrapy.Field()
    link = scrapy.Field()






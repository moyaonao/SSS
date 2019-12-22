# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from selenium import webdriver
import time
from wangyi.items import WangyiItem

class WangySpider(scrapy.Spider):
    name = 'wangy'
    # allowed_domains = ['dajie.com/']
    start_urls = ['https://m.51job.com/search/joblist.php?keyword=python&keywordtype=2&jobarea=080200']

    def parse(self, response):
        #数据处理
        job_data = response.xpath('//*[@id="pageContent"]/div[3]/a')

        for job in job_data:
            item = {}
            item['position'] = job.xpath('./h3/span/label/text()').extract_first()+job.xpath('./h3/span/text()').extract_first()
            item['pay'] = job.xpath('./em/text()').extract_first()
            item['company'] = job.xpath('./aside/text()').extract_first()
            item['area'] = job.xpath('./i/text()').extract_first()
            item['link'] = job.xpath('./@href').extract_first()
            # yield item
            yield scrapy.Request(
                url = item['link'],
                callback = self.parse_detail,
                meta = {'item':item}
            )


    def parse_detail(self,response):
        item = response.meta['item']
        h = etree.HTML(response.text)
        _h = h.xpath('//article/p/text()')
        item['desc'] = _h
        yield item


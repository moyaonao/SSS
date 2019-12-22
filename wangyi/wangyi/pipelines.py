# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class WangyiPipeline(object):
    def __init__(self):
        self.file = open('pythonjob_list.txt','w')

    def process_item(self, item, spider):
        item = dict(item)
        job_list = json.dumps(item,ensure_ascii=False) + ",\n"
        self.file.write(job_list)
        return item

    def __del__(self):
        self.file.close()

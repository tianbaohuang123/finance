# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import re

class FinancePipeline:
    def open_spider(self, spider):
        client = MongoClient(spider.settings.get("MONGO_HOST"), spider.settings.get("MONGO_PORT"))
        self.collection_fc = client["finance"]["forecast"]
        self.collection_zjh = client["finance"]["zjh"]

    def process_item(self, item, spider):
        # if isinstance(item, FinanceItem):
        if spider.name == "forecast":
            # print(dict(item))
            self.collection_fc.insert(dict(item))
        elif spider.name == "zjh":
            # print(dict(item))
            # print(item["code_stock"], item["pe_stock"], item["pb_stock"])
            item["pe_stock"] = self.process_content(item["pe_stock"])
            item["pb_stock"] = self.process_content(item["pb_stock"])
            self.collection_zjh.insert(dict(item))

        return item

    def process_content(self, content):
        content = re.sub(r"\s", "", content)
        return content

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ForecastItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code_stock = scrapy.Field()
    year = scrapy.Field()
    predict_num = scrapy.Field()
    min_EPS = scrapy.Field()
    avg_EPS = scrapy.Field()
    max_EPS = scrapy.Field()
    avg_industry_EPS = scrapy.Field()

    min_RP = scrapy.Field()
    avg_RP = scrapy.Field()
    max_RP = scrapy.Field()
    avg_industry_RP = scrapy.Field()

class PePbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code_stock = scrapy.Field()
    code_industry = scrapy.Field()
    pe_industry = scrapy.Field()
    pe_stock = scrapy.Field()
    pb_stock = scrapy.Field()
    pb_industry = scrapy.Field()
    date_time = scrapy.Field()

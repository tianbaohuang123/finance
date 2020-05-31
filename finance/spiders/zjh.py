# -*- coding: utf-8 -*-
import scrapy
from finance.items import PePbItem
import re
from finance.settings import SR_CODE_STOCK



class ZjhSpider(scrapy.Spider):
    name = 'zjh'
    allowed_domains = ['csindex.com.cn']

    # stor pe pb info
    dict_code_industry_and_pe = {}
    dict_code_industry_and_pb = {}

    # get stock total numbers
    num_of_stocks = SR_CODE_STOCK.index.array[-1] + 1
    # index_stock = 0
    index_stock = SR_CODE_STOCK.index.array[0]
    code_stock = SR_CODE_STOCK[index_stock]

    # trade_day
    trade_day = None

    # pe and pb web urls
    start_urls = ['http://www.csindex.com.cn/zh-CN/downloads/industry-price-earnings-ratio?type=zjh2']
    url_industry_pb = 'http://www.csindex.com.cn/zh-CN/downloads/industry-price-earnings-ratio?type=zjh3'

    def parse(self, response):
        # get trade date
        self.trade_day = re.findall(";date=(\d{4}-\d{2}-\d{2})", response.body.decode())[0]

        # download industry_pe
        self.get_child_code(response, self.dict_code_industry_and_pe)

        # download industry_pb
        yield scrapy.Request(
            self.url_industry_pb,
            callback=self.parse_industry_pb,
        )

    def parse_industry_pb(self, response):

        self.get_child_code(response, self.dict_code_industry_and_pb)

        stock_url = 'http://www.csindex.com.cn/zh-CN/downloads/industry-price-earnings-ratio-detail?date={}&search=1&csrc_code={}'.format(self.trade_day, self.code_stock)

        yield scrapy.Request(
            stock_url,
            callback=self.parse_child_industry_data,
        )

    def parse_child_industry_data(self, response):

        # loop find stock industry_code then get pe and pb
        item = PePbItem()
        item["code_stock"] = str(self.code_stock)
        item["code_industry"] = response.xpath("//tbody[@class='tc']/tr/td[6]/text()").extract_first()
        # item["pe_stock"] = re.sub('\s', '', response.xpath("//tbody[@class='tc']/tr/td[9]/text()").extract_first())
        # item["pb_stock"] = re.sub('\s', '', response.xpath("//tbody[@class='tc']/tr/td[10]/text()").extract_first())

        item["pe_stock"] = response.xpath("//tbody[@class='tc']/tr/td[9]/text()").extract_first()
        item["pb_stock"] = response.xpath("//tbody[@class='tc']/tr/td[10]/text()").extract_first()

        item["pe_industry"] = self.dict_code_industry_and_pe[item["code_industry"]]
        item["pb_industry"] = self.dict_code_industry_and_pb[item["code_industry"]]

        item['date_time'] = self.trade_day

        yield item

        self.index_stock += 1
        if self.index_stock >= self.num_of_stocks:
            return

        self.code_stock = self.settings["SR_CODE_STOCK"][self.index_stock]

        next_url = 'http://www.csindex.com.cn/zh-CN/downloads/industry-price-earnings-ratio-detail?date={}&search=1&csrc_code={}'.format(self.trade_day, self.code_stock)

        yield scrapy.Request(
            next_url,
            callback=self.parse_child_industry_data
        )

    def get_child_code(self, response, dict_data):

        l_table_industry = response.xpath("//table[@class='table table-bg p_table table-bordered table-border mb-20']"
                                          "/tbody/tr/td/table[@class='list-div-table']")

        l_div_industry = response.xpath("//table[@class='table table-bg p_table table-bordered table-border mb-20']"
                                        "/tbody/tr/td/div[@class='div1']")

        for table_industry, div_industry in zip(l_table_industry, l_div_industry):
            pre_fix = table_industry.xpath("./tbody/tr/td[1]/div/text()").extract_first()
            l_child_table_industry = div_industry.xpath("./table")
            for child_table_industry in l_child_table_industry:
                post_fix = child_table_industry.xpath("./tbody/tr/td[1]/div/text()").extract_first()
                pe_pb_child_industry = child_table_industry.xpath("./tbody/tr/td[3]/div/text()").extract_first()
                child_code = '' + pre_fix + post_fix
                dict_data[child_code] = re.sub('\s', '', pe_pb_child_industry)

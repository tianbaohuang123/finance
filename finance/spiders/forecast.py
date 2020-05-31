# -*- coding: utf-8 -*-
import scrapy
from finance.items import ForecastItem
from finance.settings import SR_CODE_STOCK


class ForecastSpider(scrapy.Spider):
    name = 'forecast'
    allowed_domains = ['10jqka.com.cn']
    # index_stock = 0
    index_stock = SR_CODE_STOCK.index.array[0]
    num_of_stocks = SR_CODE_STOCK.index.array[-1] + 1
    code_stock = SR_CODE_STOCK[index_stock]
    start_urls = ['http://basic.10jqka.com.cn/{}/worth.html'.format(code_stock)]

    def parse(self, response):
        # get eps and rp list by xpath
        l_tr_eps = response.xpath("//div[@class='clearfix']/div[@class='fl yjyc']/table/tbody/tr")
        l_tr_rp = response.xpath("//div[@class='clearfix']/div[@class='fr yjyc']/table/tbody/tr")
        for tr_eps,  tr_rp in zip(l_tr_eps, l_tr_rp):
            item = ForecastItem()
            item["code_stock"] = str(self.code_stock)
            # forecast earnings per share(EPS)
            item["year"] = tr_eps.xpath("./th/text()").extract_first()
            item["predict_num"] = tr_eps.xpath("./td[1]/text()").extract_first()
            item["min_EPS"] = tr_eps.xpath("./td[2]/text()").extract_first()
            item["avg_EPS"] = tr_eps.xpath("./td[3]/text()").extract_first()
            item["max_EPS"] = tr_eps.xpath("./td[4]/text()").extract_first()
            item["avg_industry_EPS"] = tr_eps.xpath("./td[5]/text()").extract_first()

            # forecast earnings retained profits
            item["min_RP"] = tr_rp.xpath("./td[2]/text()").extract_first()
            item["avg_RP"] = tr_rp.xpath("./td[3]/text()").extract_first()
            item["max_RP"] = tr_rp.xpath("./td[4]/text()").extract_first()
            item["avg_industry_RP"] = tr_rp.xpath("./td[5]/text()").extract_first()

            # print("index: " + str(self.index_stock))
            yield item

        self.index_stock += 1
        if self.index_stock >= self.num_of_stocks:
            return

        self.code_stock = self.settings["SR_CODE_STOCK"][self.index_stock]

        print("index: " + str(self.index_stock))
        print("code_stock: " + str(self.code_stock))

        next_url = 'http://basic.10jqka.com.cn/{}/worth.html'.format(self.code_stock)
        yield scrapy.Request(
            next_url,
            callback=self.parse
        )

# -*- coding: utf-8 -*-

# Scrapy settings for finance project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import tushare as ts
import pandas as pd

sr_stocks = None

try:
    with open('./stocks.csv', 'r') as f:
        sr_stocks = pd.read_csv(f, encoding="utf-8")['0']
        sr_stocks = sr_stocks.map(lambda x: str(x).zfill(6)) # csv lose prefix "0"
except Exception:
    df_hs300s = ts.get_hs300s().loc[:,["code","name"]]
    df_sz50s = ts.get_sz50s().loc[:,["code","name"]]
    df_zz500s = ts.get_zz500s().loc[:,["code","name"]]
    df_sme_classified = ts.get_sme_classified().loc[:,["code","name"]]
    df_stocks = pd.concat([df_hs300s, df_sz50s, df_zz500s, df_sme_classified]).drop_duplicates("code")
    sr_stocks = pd.Series(df_stocks.code.values)
    sr_stocks.to_csv('stocks.csv', index=False, encoding="utf-8")

SR_CODE_STOCK = sr_stocks
# print(SR_CODE_STOCK)
# SR_CODE_STOCK = sr_stocks.head(10)

BOT_NAME = 'finance'
MONGO_HOST = "localhost"
MONGO_PORT = 27017

SPIDER_MODULES = ['finance.spiders']
NEWSPIDER_MODULE = 'finance.spiders'

LOG_LEVEL = 'WARNING'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = ""
USER_AGENTS_LIST = [ "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    # 'finance.middlewares.FinanceSpiderMiddleware': 543,
#    'finance.middlewares.RandomUserAgentMiddleware': 543,
#    'finance.middlewares.CheckUserAgent': 544,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'finance.middlewares.FinanceDownloaderMiddleware': 543,
    'finance.middlewares.RandomUserAgentMiddleware': 543,
    # 'finance.middlewares.CheckUserAgent': 544,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'finance.pipelines.FinancePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

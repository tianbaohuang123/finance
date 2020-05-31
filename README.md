# finance
scrapy of finance

. <br/>
├── finance <br/>
│   ├── __init__.py <br/>
│   ├── items.py             --- **forecast item and pe & pb item** <br/>
│   ├── middlewares.py       --- **agent middleware** <br/>
│   ├── pipelines.py         --- **deal scrapy data** <br/>
│   ├── settings.py          --- **global params** <br/>
│   └── spiders <br/>
│       ├── forecast.py      --- **spider of forecast data** <br/>
│       ├── __init__.py <br/>
│       └── zjh.py           --- **spider of pe pb data** <br/>
├── finance_zjh.csv          --- **export from mongodb after run zjh spider** <br/>
├── finance_forecast.csv     --- **export from mongodb after run forecast spider** <br/>
├── scrapy.cfg <br/>
└── stocks.csv               --- **create after any spider** <br/>

## how to use
* step1: clone code
* step2: run scrapy crawl zjh
* step3: run scrapy crawl forecast
* * step2 and step3 need install scrapy, mongodb, pandas and some related tools or packages
* step4: export data from mongodb after run spider
```python
finance$ scrapy crawl zjh
finance$ scrapy crawl forecast
finance$ mongoexport -h localhost -d finance -c zjh -o finance_zjh.csv --type=csv -f code_stock,code_industry,pe_stock,pb_stock,pe_industry,pb_industry,date_time
finance$ mongoexport -h localhost -d finance -c forecast -o finance_forecast.csv --type=csv -f code_stock,year,predict_num,min_EPS,avg_EPS,max_EPS,avg_industry_EPS,min_RP,avg_RP,max_RP,avg_industry_RP
```

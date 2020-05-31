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
├── finance_zjh.csv          --- **create after run zjh spider** <br/>
├── scrapy.cfg <br/>
└── stocks.csv               --- **create after any spider** <br/>

## how to use
* step1: clone code
* step2: run scrapy crawl zjh
* step3: run scrapy crawl forecast
* * step2 and step3 need install scrapy, mongodb, pandas and some related tools or packages

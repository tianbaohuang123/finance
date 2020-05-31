# finance
scrapy of finance

.
├── finance
│   ├── __init__.py
│   ├── items.py             **forecast item and pe & pb item**
│   ├── middlewares.py       **agent middleware**
│   ├── pipelines.py         **deal scrapy data**
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── items.cpython-36.pyc
│   │   ├── middlewares.cpython-36.pyc
│   │   ├── pipelines.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── settings.py           **global params**
│   └── spiders
│       ├── forecast.py       **spider of forecast data**
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── forecast.cpython-36.pyc
│       │   ├── __init__.cpython-36.pyc
│       │   └── zjh.cpython-36.pyc
│       └── zjh.py            **spider of pe pb data**
├── finance_zjh.csv           **create after run zjh spider**
├── scrapy.cfg
└── stocks.csv                **create after any spider**

## how to use
* step1: clone code
* step2: run scrapy crawl zjh
* step3: run scrapy crawl forecast
* * step2 and step3 need install scrapy, mongodb, pandas and some related tools or packages

# 描述
##### Language : Python 2.7
##### Framework : Scrapy 1.4

# 更改説明
> 1.在middlewares.py中加入自己的cookie(需要在浏览中找)  
> 2.如果要存入mongodb,在pipelines_mongodb.py中加入mongodb config

# 创建独立python环境
```bash
cd ./nightcrawler/EvaluateCrawl
pip install virtualenv
virtualenv --no-site-packages venv
```



# 运行
```bash
cd nightcrawler/EvaluateCrawl
source venv/bin/active
pip install scrapy
scrapy crawl tb_spider
scrapy crawl tm_spider
scrapy crawl jd_spider
```
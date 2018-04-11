# -*- coding: utf-8 -*-

# Scrapy settings for EvaluateCrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import json
def load():
    with open('./setting.json') as json_file:
        data = json.load(json_file)
        return data
json_data = load()
print json_data
ALI_QUERY_WORDS = json_data['ALI_QUERY_WORDS']
JD_QUERY_WORDS = json_data['JD_QUERY_WORDS']
TM_COOKIE = json_data['TM_COOKIE']
TB_ITEM_COOKIE = json_data['TB_ITEM_COOKIE']
TB_COMMENT_COOKIE = json_data['TB_COMMENT_COOKIE']
# ALI_QUERY_WORDS = ['小米小爱智能音箱','天猫精灵x1','喜马拉雅小雅音响','问问智能音箱','叮咚智能音箱','rokid智能音箱','小鱼在家','小度在家']
# JD_QUERY_WORDS = ['小米小爱','小雅智能音响','问问智能音箱','叮咚智能音箱','rokid智能','小鱼在家','小度在家']
#从浏览器复制cookie到这里
# TM_COOKIE = "thw=cn; UM_distinctid=15f1f4827f2480-06cffffa4ce0d8-3e63430c-1fa400-15f1f4827f46d7; miid=2199199762545191723; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=guige154512997; t=840f7b431b9be576913e177fd20ecb0a; tg=0; cna=xINjEsHOg0cCAQ4XJ2reCLu6; v=0; cookie2=1510d40357d5ee73d7348f515c79bf96; _tb_token_=e1ee37450313b; lgc=guige154512997; _m_h5_tk=6daa03a9e2002a7964da427168ebcadd_1514880548298; _m_h5_tk_enc=4be2eb99b193fa5ea79928292d3bc6ca; uc1=cookie14=UoTdf1kEFFJguQ%3D%3D&lng=zh_CN&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&cookie21=Vq8l%2BKCLiv0Mzbofagu7Fg%3D%3D&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0; uc3=sg2=BdZTQmoyHJzAx3ektBCIaLpuvy06UAB7SYTLqUAsHHw%3D&nk2=BIOAPwBAvid%2Bh7Yva%2BQ%3D&id2=VWeWRRSlqSdw&vt3=F8dBzLeJQAqfHBksIxA%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTUxNDg4NDMwNg%3D%3D; uss=VAYuzNUjBj6f4zk5V36EfNQoP9tCHlkGV6NNEnu9d0kLXFeZK5tK%2FXkkRg%3D%3D; sg=77c; mt=np=&ci=6_1; cookie1=AC5Q%2FDLWcg%2BZN%2BPVokoT3YaAE7GpJmcejKrC142kGdc%3D; unb=687100117; skt=fe41b85978d4f2ec; _cc_=UIHiLt3xSw%3D%3D; _l_g_=Ug%3D%3D; _nk_=guige154512997; cookie17=VWeWRRSlqSdw; isg=AmtrPnpWtfmlF-rODrN4Jiw_-o-VKH-W_YaiI93oTqoBfIveZVAPUgncqovo"
# TB_ITEM_COOKIE = "thw=cn; UM_distinctid=15f1f4827f2480-06cffffa4ce0d8-3e63430c-1fa400-15f1f4827f46d7; miid=2199199762545191723; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=guige154512997; t=840f7b431b9be576913e177fd20ecb0a; tg=0; cna=xINjEsHOg0cCAQ4XJ2reCLu6; v=0; cookie2=1510d40357d5ee73d7348f515c79bf96; _tb_token_=e1ee37450313b; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; uc3=sg2=BdZTQmoyHJzAx3ektBCIaLpuvy06UAB7SYTLqUAsHHw%3D&nk2=BIOAPwBAvid%2Bh7Yva%2BQ%3D&id2=VWeWRRSlqSdw&vt3=F8dBzLeJQZCHd5D9ovw%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; existShop=MTUxNDg3NTA3OQ%3D%3D; uss=VAYuzNUjBj6f4zk5V36EfNQoP9tCHlkGV6NNEnu9d0kLXFeZK5tK%2FXkkRg%3D%3D; lgc=guige154512997; sg=77c; cookie1=AC5Q%2FDLWcg%2BZN%2BPVokoT3YaAE7GpJmcejKrC142kGdc%3D; unb=687100117; skt=052bb16428909a1f; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; _nk_=guige154512997; cookie17=VWeWRRSlqSdw; mt=ci=6_1; uc1=cookie14=UoTdf1kLPk1rYw%3D%3D&lng=zh_CN&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&cookie21=Vq8l%2BKCLiv0Mzbofagu7Fg%3D%3D&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; _m_h5_tk=6daa03a9e2002a7964da427168ebcadd_1514880548298; _m_h5_tk_enc=4be2eb99b193fa5ea79928292d3bc6ca; isg=AicnCutvMXV0jrYaKm98GhCLtlsxBPsaUZKel_mVu7bZ6E-qAX0b37modt8M; JSESSIONID=D17E7576835A6DE397FD5D85D3EA8891"
# TB_COMMENT_COOKIE = "thw=cn; UM_distinctid=15f1f4827f2480-06cffffa4ce0d8-3e63430c-1fa400-15f1f4827f46d7; miid=2199199762545191723; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=guige154512997; t=840f7b431b9be576913e177fd20ecb0a; tg=0; cna=xINjEsHOg0cCAQ4XJ2reCLu6; v=0; cookie2=1510d40357d5ee73d7348f515c79bf96; _tb_token_=e1ee37450313b; uc3=sg2=BdZTQmoyHJzAx3ektBCIaLpuvy06UAB7SYTLqUAsHHw%3D&nk2=BIOAPwBAvid%2Bh7Yva%2BQ%3D&id2=VWeWRRSlqSdw&vt3=F8dBzLeJQZCHd5D9ovw%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; existShop=MTUxNDg3NTA3OQ%3D%3D; uss=VAYuzNUjBj6f4zk5V36EfNQoP9tCHlkGV6NNEnu9d0kLXFeZK5tK%2FXkkRg%3D%3D; lgc=guige154512997; sg=77c; cookie1=AC5Q%2FDLWcg%2BZN%2BPVokoT3YaAE7GpJmcejKrC142kGdc%3D; unb=687100117; skt=052bb16428909a1f; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; _nk_=guige154512997; cookie17=VWeWRRSlqSdw; mt=ci=6_1; uc1=cookie14=UoTdf1kLPk1rYw%3D%3D&lng=zh_CN&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&cookie21=Vq8l%2BKCLiv0Mzbofagu7Fg%3D%3D&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; _m_h5_tk=6daa03a9e2002a7964da427168ebcadd_1514880548298; _m_h5_tk_enc=4be2eb99b193fa5ea79928292d3bc6ca; isg=AtbWfQJUkOqtLqetswS91VngJ4wY3xolaKmvgEA-I7lQA3GdqAaowOax56gV"


BOT_NAME = 'EvaluateCrawl'

SPIDER_MODULES = ['EvaluateCrawl.spiders']
NEWSPIDER_MODULE = 'EvaluateCrawl.spiders'




# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063']


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'EvaluateCrawl.middlewares.EvaluatecrawlSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'EvaluateCrawl.middlewares.UserAgentMiddleware': 542,
    # 'EvaluateCrawl.middlewares.IPMiddleware': 543,
    'EvaluateCrawl.middlewares.CookiesMiddleware': 544,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'EvaluateCrawl.pipelines_mongodb.SpiderPipeline': 300,
   'EvaluateCrawl.pipelines_csv.SpiderPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

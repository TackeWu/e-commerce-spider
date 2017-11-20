#!/usr/bin/env bash


~/venv/bin/scrapy crawl tb_spider > tb_run.log 2>&1
~/venv/bin/scrapy crawl tm_spider > tm_run.log 2>&1
~/venv/bin/scrapy crawl jd_spider > jd_run.log 2>&1
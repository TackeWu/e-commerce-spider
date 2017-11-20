# -*- coding: utf-8 -*-
import scrapy
import requests
import json
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from EvaluateCrawl.settings import ALI_QUERY_WORDS
from EvaluateCrawl.items import TmallItem,TmallCommentItem


class Spider(scrapy.Spider):
    name = 'tm_spider'
    allowed_domains = ['taobao.com','tmall.com','rate.tmall.com','s.taobao.com']

    def start_requests(self):
        for query in ALI_QUERY_WORDS:
            query_url = "https://list.tmall.com/search_product.htm?q="+str(query)+"&sort=d&style=g&industryCatId=all"
            yield scrapy.Request(query_url,callback=self.Item_parse,meta={"query_words":query},encoding='utf-8')


    def Item_parse(self, response):
        item = TmallItem()
        item['Searchterms'] = []
        item['Storename'] = []
        item['Itemwords'] = []
        item['Itemlink'] = []
        item['Itemnid'] = []
        item['Salesvolume'] = []
        item['Price'] = []
        item['Commentpage'] = []
        item['Commentcount'] = []

        ItemList = response.xpath('//div[@id="J_ItemList"]')
        for sub_div in ItemList.xpath('.//div[@class="product item-1111 "]'):
            item['Searchterms'].append(response.meta['query_words'])
            item['Storename'].append(sub_div.xpath('.//span[@data-icon="small"]/@data-nick').extract()[0])
            item['Itemwords'].append(sub_div.xpath('.//p[@class="productTitle"]/a/@title').extract()[0])
            item['Itemlink'].append(sub_div.xpath('.//p[@class="productTitle"]/a/@href').extract()[0])
            nid = sub_div.xpath('.//@data-id').extract()[0]
            item['Itemnid'].append(nid)
            item['Salesvolume'].append(sub_div.xpath('.//p[@class="productStatus"]/span/em/text()').extract()[0])
            item['Price'].append(sub_div.xpath('.//p[@class="productPrice"]/em/@title').extract()[0])
            item['Commentcount'].append(sub_div.xpath('.//p[@class="productStatus"]/span/a/text()').extract()[0])

            comment_url = "https://rate.tmall.com/list_detail_rate.htm?itemId=" + str(nid) + "&sellerId=" + str(nid) + "&order=1&currentPage=1"
            req_comment = requests.get(comment_url)
            try:
                site = json.loads("{" + req_comment.text + "}")
            except ValueError:
                continue
            sites = site['rateDetail']
            item['Commentpage'].append(sites['paginator']['lastPage'])
            for page in range(1, sites['paginator']['lastPage'] + 1):
                page_url = "https://rate.tmall.com/list_detail_rate.htm?itemId=" + str(nid) + "&sellerId=" + str(nid) + "&order=1&currentPage=" + str(page)
                yield scrapy.Request(page_url, callback=self.tmall_comment_parse,meta={"nid": nid, "query_words": response.meta['query_words']},encoding='utf-8')
        yield item


    def tmall_comment_parse(self,response):
        item = TmallCommentItem()
        item['Itemnid'] = []
        item['UserName'] = []
        item['Commentdate'] = []
        item['Setmeal'] = []
        item['Conntent'] = []
        item['Commenttimestamp'] = []
        item['Tradeendtimestamp'] = []
        item['Searchterms'] = []
        try:
            site = json.loads('{'+response.body_as_unicode()+'}')
            if site != None and site != []:
                sites = site['rateDetail']["rateList"]
                for site in sites:
                    item['Itemnid'].append(response.meta['nid'])
                    item['Searchterms'].append(response.meta['query_words'])
                    item['UserName'].append(site['displayUserNick'])
                    item['Commentdate'].append(site['rateDate'])
                    item['Setmeal'].append(site['auctionSku'])
                    item['Conntent'].append(site['rateContent'])
                    item['Commenttimestamp'].append(site['gmtCreateTime'])
                    item['Tradeendtimestamp'].append(site['tradeEndTime'])
            yield  item
        except ValueError:
            pass



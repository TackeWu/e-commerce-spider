# -*- coding: utf-8 -*-
import scrapy
import requests
import json
import logging
from EvaluateCrawl.settings import JD_QUERY_WORDS

from EvaluateCrawl.items import JDItem,JDCommentItem



class Spider(scrapy.Spider):
    name = 'jd_spider'
    allowed_domains = ['jd.com','search.jd.com','club.jd.com',]


    def start_requests(self):
        for query in JD_QUERY_WORDS:
            query_url = "https://search.jd.com/Search?keyword=%s&enc=utf-8&psort=3" % query
            yield scrapy.Request(query_url,callback=self.JD_parse,meta={"query_words":query},encoding='utf-8')

    def JD_parse(self,response):
        item = JDItem()
        res_ul = response.xpath('//ul[@class="gl-warp clearfix"]')

        item['Searchterms'] = []
        item['Storename'] = []
        item['Itemid'] = []
        item['Promowords'] = []
        item['Price'] = []
        item['Commenturl'] = []
        item['Itemurl'] = []
        item['Itemwords'] = []
        item['Hotcomment'] = []
        item['Commentcount'] = []
        for ul in res_ul.xpath('.//li[@class="gl-item"]'):
            hot_comment = []
            item['Searchterms'].append(response.meta['query_words'])
            item_id = ul.xpath('@data-sku').extract()
            item['Itemid'].append(item_id[0])
            try:
                item['Promowords'].append(ul.xpath('.//div[@class="p-name p-name-type-2"]/a/i[@class="promo-words"]/text()').extract()[0])
            except IndexError:
                item['Promowords'].append(None)
            try:
                item['Price'].append(ul.xpath('.//div[@class="p-price"]/strong/i/text()').extract()[0])
            except IndexError:
                item['Price'].append(None)
            try:
                item['Storename'].append(ul.xpath('.//div[@class="p-shop"]/span/a/text()').extract()[0])
            except IndexError:
                item['Storename'].append(None)
            item['Itemurl'].append("https:"+ul.xpath('.//div[@class="p-name p-name-type-2"]/a/@href').extract()[0])
            item['Commenturl'].append("http:"+ul.xpath('.//div[@class="p-commit"]/strong/a/@href').extract()[0])
            re = ""
            for i in ul.xpath('.//div[@class="p-name p-name-type-2"]/a/em/text()').extract():
                re = re + i
            item['Itemwords'].append(re)
            page_url = "https://club.jd.com/comment/skuProductPageComments.action?productId="+str(item_id[0])+"&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
            try:
                site = requests.get(page_url)
                sites_json = json.loads(site.text)
                comment_count = sites_json['productCommentSummary']['commentCount']
                item['Commentcount'].append(comment_count)
                sites_page = int(comment_count)/10
                for i in sites_json['hotCommentTagStatistics']:
                    hot_comment.append({"name":i['name'],"count":i['count']})
                item['Hotcomment'].append(hot_comment)
                for page in range(0,int(sites_page)+11):
                    comment_url = "https://club.jd.com/comment/skuProductPageComments.action?productId="+str(item_id[0])+"&score=0&sortType=5&page="+str(page)+"&pageSize=10&isShadowSku=0&fold=1"
                    yield scrapy.Request(comment_url,callback=self.JD_comment_parse,encoding='utf-8',meta={"query_words":response.meta['query_words']})
            except ValueError:
                continue
        yield item

    def JD_comment_parse(self,response):
        item = JDCommentItem()
        sites_json = json.loads(response.body_as_unicode())
        sites_dict = dict(sites_json)
        if sites_dict['comments'] != []:
            item['Itemid'] = []
            item['Searchterms'] = []
            item['Userid'] = []
            item['Nickname'] = []
            item['Content'] = []
            item['Commenttime'] = []
            item['Referencename'] = []
            item['Referencetime'] = []
            item['Userlevel'] = []
            item['Ismobile'] = []
            item['Userclient'] = []
            item['Isreplies'] = []
            item['Repliescontent'] = []
            item['Isordercomment'] = []
            item['Ordercommentcontent'] = []
            comments = sites_json['comments']
            try :
                for comment in comments:
                    item['Itemid'].append(comment['referenceId'])
                    item['Searchterms'].append(response.meta['query_words'])
                    item['Userid'].append(comment['id'])
                    item['Nickname'].append(comment['nickname'])
                    item['Content'].append(comment['content'])
                    item['Commenttime'].append(comment['creationTime'])
                    item['Referencename'].append(comment['referenceName'])
                    item['Referencetime'].append(comment['referenceTime'])
                    item['Userlevel'].append(comment['userLevelName'])
                    item['Ismobile'].append(comment['isMobile'])
                    item['Userclient'].append(comment['userClientShow'])
                    if comment.has_key('replies') and comment['replies'] != []:
                        item['Isreplies'].append(True)
                        re = ""
                        for replie in comment['replies']:
                            re = re + replie['content']
                        item['Repliescontent'].append(re)
                    else:
                        item['Isreplies'].append(False)
                        item['Repliescontent'].append(None)
                    if comment.has_key('showOrderComment') and comment['showOrderComment'] != []:
                        item['Isordercomment'].append(True)
                        item['Ordercommentcontent'].append(comment['showOrderComment']['content'])
                    else:
                        item['Isordercomment'].append(False)
                        item['Ordercommentcontent'].append(None)

            except TypeError:
                logging.warning("TypeError")
            finally:
                yield item
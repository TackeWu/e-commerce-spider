# -*- coding: utf-8 -*-
import scrapy
import requests
import json
import re
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from EvaluateCrawl.settings import ALI_QUERY_WORDS

from EvaluateCrawl.items import TaobaoItem,TaobaoCommentItem

class Spider(scrapy.Spider):
    name = 'tb_spider'
    allowed_domains = ['taobao.com','tmall.com','rate.tmall.com','s.taobao.com']

    def start_requests(self):
        for query in ALI_QUERY_WORDS:
            query_url = "https://s.taobao.com/search?data-key=sort&data-value=sale-desc&ajax=true&q=%s" % query
            yield scrapy.Request(query_url,callback=self.Item_parse,meta={"query_words":query,"name" : "item"},encoding='utf-8')


    def Item_parse(self, response):
        item = TaobaoItem()
        sites_json = json.loads(response.body_as_unicode())
        sites_dict = dict(sites_json)
        if sites_dict.has_key('mods'):
            sites_list = sites_dict['mods']['itemlist']['data']['auctions']
            item['Searchterms'] = []
            item['Storename'] = []
            item['Storekeeperid'] = []
            item['Itemwords'] = []
            item['Itemlink'] = []
            item['Itemnid'] = []
            item['Salesvolume'] = []
            item['Price'] = []
            item['Location'] = []
            item['Istmall'] = []
            item['Totalrate'] = []
            item['Commentpage'] = []
            item['Commentcount'] = []
            for iter in sites_list:
                if iter['shopcard']['isTmall'] == False:
                    item['Searchterms'].append(response.meta['query_words'])
                    item['Storename'].append(iter['nick'])
                    item['Storekeeperid'].append(iter['user_id'])
                    item['Itemwords'].append(iter['raw_title'])
                    item['Itemlink'].append("https:"+iter['detail_url'])
                    item['Itemnid'].append(iter['nid'])
                    item['Salesvolume'].append(iter['view_sales'])
                    item['Price'].append(iter['view_price'])
                    item['Location'].append(iter['item_loc'])
                    item['Commentcount'].append(iter['comment_count'])
                    item['Istmall'].append(iter['shopcard']['isTmall'])
                    item['Totalrate'].append(iter['shopcard']['totalRate'])
                    comment_url = "https://rate.taobao.com/feedRateList.htm?auctionNumId="+str(iter['nid'])+"&currentPageNum=1&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0"
                    requests.get("https:"+iter['detail_url'])
                    req_comment = requests.get(comment_url)
                    try:
                        site = json.loads(re.search(".*?\((.*)\).*?", req_comment.text).group(1))
                    except AttributeError:
                        continue
                    if int(site['maxPage'])%20 != 0:
                        temp = 1
                    else:
                        temp = 0
                    item['Commentpage'].append(int(site['maxPage'])/20+temp)
                    for page in range(1,int(site['maxPage'])/20+temp+1):
                        comment_url = "https://rate.taobao.com/feedRateList.htm?auctionNumId=" + str(iter['nid']) + "&currentPageNum="+str(page)+"&pageSize=20&rateType=&orderType=feedbackdate&attribute=&sku=&hasSku=false&folded=0"
                        yield scrapy.Request(comment_url,callback=self.taobao_comment_parse,meta={"nid":iter['nid'],"query_words":response.meta['query_words'],"name" : "comment"})

            yield item

    def taobao_comment_parse(self,response):
        item = TaobaoCommentItem()
        item['Itemnid'] = []
        item['Searchterms'] = []
        item['UserName'] = []
        item['Commentdate'] = []
        item['Setmeal'] = []
        item['Conntent'] = []
        try:
            sites = json.loads(re.search(".*?\((.*)\).*?", response.body_as_unicode()).group(1))
            comments = sites['comments']
            for comment in comments:
                item['Itemnid'].append(response.meta['nid'])
                item['Searchterms'].append(response.meta['query_words'])
                item['UserName'].append(comment['user']['nick'])
                item['Commentdate'].append(comment['date'])
                item['Setmeal'].append(comment['auction']['sku'])
                item['Conntent'].append(comment['content'])
            yield item
        except AttributeError:
            pass




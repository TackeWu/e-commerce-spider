# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Searchterms = scrapy.Field()
    Storename = scrapy.Field()
    Storekeeperid = scrapy.Field()
    Itemwords = scrapy.Field()
    Itemlink = scrapy.Field()
    Itemnid = scrapy.Field()
    Salesvolume = scrapy.Field()
    Price = scrapy.Field()
    Location = scrapy.Field()
    Commentpage = scrapy.Field()
    Commentcount = scrapy.Field()
    Totalrate = scrapy.Field()
    Istmall = scrapy.Field()

class TaobaoCommentItem(scrapy.Item):
    Itemnid = scrapy.Field()
    Searchterms = scrapy.Field()
    UserName = scrapy.Field()
    Commentdate = scrapy.Field()
    Setmeal = scrapy.Field()
    Conntent = scrapy.Field()

class TmallItem(scrapy.Item):
    Searchterms = scrapy.Field()
    Storename = scrapy.Field()
    Itemwords = scrapy.Field()
    Itemlink = scrapy.Field()
    Itemnid = scrapy.Field()
    Salesvolume = scrapy.Field()
    Price = scrapy.Field()
    Commentpage = scrapy.Field()
    Commentcount = scrapy.Field()

class TmallCommentItem(scrapy.Item):
    Itemnid = scrapy.Field()
    Searchterms = scrapy.Field()
    UserName = scrapy.Field()
    Commentdate = scrapy.Field()
    Setmeal = scrapy.Field()
    Conntent = scrapy.Field()
    Commenttimestamp = scrapy.Field()
    Tradeendtimestamp = scrapy.Field()

class JDItem(scrapy.Item):
    Searchterms = scrapy.Field()
    Storename = scrapy.Field()
    Itemid = scrapy.Field()
    Promowords = scrapy.Field()
    Itemwords = scrapy.Field()
    Price = scrapy.Field()
    Commenturl =scrapy.Field()
    Itemurl = scrapy.Field()
    Commentcount = scrapy.Field()
    Hotcomment = scrapy.Field()

class JDCommentItem(scrapy.Item):
    Itemid = scrapy.Field()
    Searchterms = scrapy.Field()
    Userid = scrapy.Field()
    Nickname = scrapy.Field()
    Content = scrapy.Field()
    Commenttime = scrapy.Field()
    Referencename = scrapy.Field()
    Referencetime = scrapy.Field()
    Userlevel = scrapy.Field()
    Ismobile = scrapy.Field()
    Userclient = scrapy.Field()
    Isreplies = scrapy.Field()
    Repliescontent = scrapy.Field()
    Isordercomment = scrapy.Field()
    Ordercommentcontent = scrapy.Field()




# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from EvaluateCrawl.dbs import NemoCfgMongoClient
from EvaluateCrawl.items import TaobaoItem,TmallItem,TmallCommentItem,TaobaoCommentItem
from EvaluateCrawl.items import JDItem,JDCommentItem
import csv
import time

class SpiderPipeline(object):
    mongo_db_ali = "data_ali"
    mongo_db_jd = "data_jd"
    str_date = time.strftime("_%m_%d", time.localtime())

    def open_spider(self,spider):

        if spider.name == "jd_spider":
            f = open('./data/jd_item'+self.str_date+'.csv','w+')
            fieldnames = JDItem().fields
            print fieldnames
            self.jd_item = csv.DictWriter(f,fieldnames=fieldnames)
            self.jd_item.writeheader()

            f = open('./data/jd_comment'+self.str_date+'.csv','w+')
            fieldnames = JDCommentItem.fields
            print fieldnames
            self.jd_comment = csv.DictWriter(f,fieldnames=fieldnames)
            self.jd_comment.writeheader()

        elif spider.name == "tb_spider":
            f = open('./data/taobao_item'+self.str_date+'.csv','w+')
            fieldnames = TaobaoItem().fields
            self.taobao_item = csv.DictWriter(f,fieldnames=fieldnames)
            self.taobao_item.writeheader()

            f = open('./data/taobao_comment'+self.str_date+'.csv','w+')
            fieldnames = TaobaoCommentItem().fields
            self.taobao_comment = csv.DictWriter(f,fieldnames=fieldnames)
            self.taobao_comment.writeheader()

        elif spider.name == "tm_spider" :
            f = open('./data/tmall_item'+self.str_date+'.csv','w+')
            fieldnames = TmallItem().fields
            self.tmall_item = csv.DictWriter(f,fieldnames=fieldnames)
            self.tmall_item.writeheader()

            f = open('./data/tmall_comment'+self.str_date+'.csv','w+')
            fieldnames = TmallCommentItem().fields
            self.tmall_comment = csv.DictWriter(f,fieldnames=fieldnames)
            self.tmall_comment.writeheader()



    def process_item(self, item, spider):
        if isinstance(item,TaobaoItem):
            len_item = len(item['Searchterms'])
            for i in range(len_item):
                item_dict = {}
                for j in item.keys():
                    if item[j] == [] or item[j] == None:
                        item_dict[j] = None
                    else :
                        try:
                            item_dict[j]=item[j][i]
                        except IndexError:
                            item_dict[j] = None
                self.taobao_item.writerow(item_dict)
            print "TaobaoItem"

        if isinstance(item,TmallItem):
            len_item = len(item['Searchterms'])
            for i in range(len_item):
                item_dict = {}
                for j in item.keys():
                    if item[j] == [] or item[j] == None:
                        item_dict[j] = None
                    else :
                        try:
                            item_dict[j]=item[j][i]
                        except IndexError:
                            item_dict[j] = None
                self.tmall_item.writerow(item_dict)
            print "TmallItem"

        elif isinstance(item,TmallCommentItem):
            len_item = len(item['Searchterms'])
            for i in range(len_item):
                item_dict = {}
                for j in item.keys():
                    if item[j] == [] or item[j] == None:
                        item_dict[j] = None
                    else :
                        try:
                            item_dict[j]=item[j][i]
                        except IndexError:
                            item_dict[j] = None
                self.tmall_comment.writerow(item_dict)
            print "TmallCommentItem"

        elif isinstance(item,TaobaoCommentItem):
            len_item = len(item['Searchterms'])
            for i in range(len_item):
                item_dict = {}
                for j in item.keys():
                    if item[j] == [] or item[j] == None:
                        item_dict[j] = None
                    else :
                        try:
                            item_dict[j]=item[j][i]
                        except IndexError:
                            item_dict[j] = None
                self.taobao_comment.writerow(item_dict)
            print "TaobaoCommentItem"

        elif isinstance(item,JDItem):
            len_item = len(item['Searchterms'])
            for i in range(len_item):
                item_dict = {}
                for j in item.keys():
                    if item[j] == [] or item[j] == None:
                        item_dict[j] = None
                    else :
                        try:
                            item_dict[j]=item[j][i]
                        except IndexError:
                            item_dict[j] = None
                self.jd_item.writerow(item_dict)
            print "JDItem"

        elif isinstance(item,JDCommentItem):
            len_item = len(item['Searchterms'])
            for i in range(len_item):
                item_dict = {}
                for j in item.keys():
                    if item[j] == [] or item[j] == None:
                        item_dict[j] = None
                    else:
                        try:
                            item_dict[j]=item[j][i]
                        except IndexError:
                            item_dict[j] = None
                self.jd_comment.writerow(item_dict)
            print "JDCommentItem"
        else :
            print("unable output")
        return item
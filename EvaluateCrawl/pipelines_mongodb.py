# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from EvaluateCrawl.items import TaobaoItem,TmallItem,TmallCommentItem,TaobaoCommentItem
from EvaluateCrawl.items import JDItem,JDCommentItem



class SpiderPipeline(object):
    mongo_db_ali = "data_ali"
    mongo_db_jd = "data_jd"

    def open_spider(self,spider):
        self.client = NemoCfgMongoClient() #monogo config
        self.db_ali = self.client[self.mongo_db_ali]
        self.db_jd = self.client[self.mongo_db_jd]
        if spider.name == "jd_spider":
            self.client.drop_database(self.mongo_db_jd)

        elif spider.name == "tb_spider":
            client = self.client
            client.data_ali.drop_collection("taobao_item")
            client.data_ali.drop_collection("taobao_comment")
        elif spider.name == "tm_spider" :
            client = self.client
            client.data_ali.drop_collection("tmall_item")
            client.data_ali.drop_collection("tmall_comment")


    def close_spider(self,spider):
        self.client.close()

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
                self.db_ali.taobao_item.insert_one(item_dict)
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
                self.db_ali.tmall_item.insert_one(item_dict)
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

                self.db_ali.tmall_comment.insert_one(item_dict)
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
                self.db_ali.taobao_comment.insert_one(item_dict)
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
                self.db_jd.item.insert_one(item_dict)
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
                self.db_jd.comment.insert_one(item_dict)
            print "JDCommentItem"
        else :
            print("unable output")
        return item
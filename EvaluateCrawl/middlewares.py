# encoding=utf-8
import json
import random
import re

class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        if spider.name == 'tb_spider' and request.meta["name"] == "item":
            cookie ={

            }#your cookie
            request.cookies = cookie
        elif spider.name == 'tb_spider' and request.meta["name"] == "comment":
            cookie = {

            }#your cookie
            request.cookies = cookie

        elif spider.name == 'tm_spider':
            cookie = {

            }#your cookie



            request.cookies = cookie


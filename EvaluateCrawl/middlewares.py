# encoding=utf-8
import json
import random
import re
import settings
from cookie_format import transCookie
class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        if spider.name == 'tb_spider' and request.meta["name"] == "item":
            tb_cookie = settings.TB_ITEM_COOKIE
            cookie = transCookie(tb_cookie).stringToDict()
            request.cookies = cookie

        elif spider.name == 'tb_spider' and request.meta["name"] == "comment":
            tm_cookie = settings.TB_COMMENT_COOKIE
            cookie = transCookie(tm_cookie).stringToDict()
            request.cookies = cookie

        elif spider.name == 'tm_spider':
            tm_cookie = settings.TM_COOKIE
            cookie = transCookie(tm_cookie).stringToDict()
            request.cookies = cookie


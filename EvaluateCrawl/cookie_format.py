#-*- coding:utf-8 -*-
import re

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie
    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            cookie_search = re.search("(.*?)=(.*)",item)
            key = cookie_search.group(1)
            value = cookie_search.group(2)
            itemDict[key] = value
        return itemDict
#! /usr/bin/python
# -*- coding: utf-8 -*

import re

import os

from htmd import htmd
from utils import urlopener


class RegCompiler(object):

    def __init__(self, context) -> None:
        super().__init__()
        self.fullcontext = context

    def getArticleUrls(self):
        fullcontext = self.fullcontext
        mainObj = re.search(r'<main.*?</main', str(fullcontext))
        articlesurls = set(re.findall(r'https://blog\.csdn\.net/.{1,100}/article/details/\d{3,10}', mainObj.group()))
        return articlesurls

    def getImgUrls(self):
        list = []
        fullcontext = self.fullcontext
        mainObj = re.search(r'<article[\d\D]*</article>', str(fullcontext))
        imgurls = set(re.findall(r'https://img-blog.csdn.net/\d{10,20}.*?\"', mainObj.group()))
        for key in imgurls:
            imgurl = re.sub(r'\".?', '', key)
            list.append(imgurl)
        return set(list)

    def getArticle(self):
        fullcontext = self.fullcontext
        mainObj = re.search(r'<article[\d\D]*</article>', fullcontext.decode('utf-8'))
        if mainObj:
            return htmd.subElements(htmd.deleteElements(mainObj.group()))
        else:
            return None

    def getArticleTitle(self):
        fullcontext = self.fullcontext
        mainObj = re.search(r'<title.*?- CSDN', fullcontext.decode('utf-8'))
        if mainObj:
            mainObj = re.sub('<title>', '', str(mainObj.group()))
            mainObj = re.sub('- CS.*', '', str(mainObj))
            mainObj = re.sub('\.', '', str(mainObj))
            mainObj = re.sub(';', '', str(mainObj))
            mainObj = re.sub(':', '', str(mainObj))
            mainObj = re.sub('/', '', str(mainObj))
            mainObj = re.sub(' ', '', str(mainObj))
            mainObj = re.sub('\\\\', '', str(mainObj))
            mainObj = re.sub('\*', '', str(mainObj))
            mainObj = re.sub('\[', '', str(mainObj))
            mainObj = re.sub('\]', '', str(mainObj))
            mainObj = re.sub(',', '', str(mainObj))
            mainObj = re.sub('，', '', str(mainObj))
            mainObj = re.sub('。', '', str(mainObj))
            mainObj = re.sub(' ', '', str(mainObj))
            return mainObj
        else:
            return None







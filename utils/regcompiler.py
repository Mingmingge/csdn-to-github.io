#! /usr/bin/python
# -*- coding: utf-8 -*

import re
from utils import urlopener


class RegCompiler(object):

    def __init__(self, url) -> None:
        super().__init__()
        self.url = url

    def getArticleUrls(self):
        myopen = urlopener.MyUrlOpen(self.url)
        fullcontext = myopen.my_UrlOpen()
        mainObj = re.search(r'<main.*?</main', str(fullcontext))
        articlesurls = set(re.findall(r'https://blog\.csdn\.net/.{1,100}/article/details/\d{8}', mainObj.group()))
        return articlesurls

    def getImgUrls(self):
        list = []
        myopen = urlopener.MyUrlOpen(self.url)
        fullcontext = myopen.my_UrlOpen()
        imgurls = set(re.findall(r'https://img-blog.csdn.net/\d{10,20}.*?\"', str(fullcontext)))
        for key in imgurls:
            imgurl = re.sub(r'\".?', '', key)
            list.append(imgurl)
        return set(list)




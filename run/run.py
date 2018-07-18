#! /usr/bin/python
# -*- coding: utf-8 -*-
from utils.articlewriter import ArticleWriter
from utils.hosttourl import hostTourl
from utils.imgwriter import ImgWriter
from utils.regcompiler import RegCompiler
from utils.urlopener import MyUrlOpen


def run():
    parenpath = '/Users/hulimin/Desktop/1234'
    host = 'https://blog.csdn.net/babybabyup'
    i = 1
    j = 0
    while 1:
        opener = MyUrlOpen(hostTourl(host, i))
        context = opener.my_UrlOpen()
        regcompiler = RegCompiler(context)
        if regcompiler.getArticleUrls():
            for key in regcompiler.getArticleUrls():
                print(key)
                j = j+1
                articleopener = MyUrlOpen(key)
                articlrcontext = articleopener.my_UrlOpen()
                articleregcompiler = RegCompiler(articlrcontext)
                if articleregcompiler.getImgUrls():
                    for imgurl in articleregcompiler.getImgUrls():
                        imgwriter = ImgWriter(imgurl, parenpath)
                        imgwriter.imgwrite()
                else:
                    print("本篇博客没有图片")

                title = articleregcompiler.getArticleTitle()
                articlemain = articleregcompiler.getArticle()
                articlewriter = ArticleWriter(articlemain, title, parenpath)
                articlewriter.articlewrite()
        else:
            print('共有%d页' %int(i-1))
            print('已经获取完毕!,共有%d个文件'%j)
            break
        i = i + 1

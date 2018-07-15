#! /usr/bin/python
# -*- coding: utf-8 -8*-
from utils.urlopener import MyUrlOpen, MyImgUrlOpen

myopen1 = MyUrlOpen('https://blog.csdn.net/babybabyup')
print(myopen1.my_UrlOpen())

myopen2 = MyImgUrlOpen('https://img-blog.csdn.net/20160601100450061?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center')
print(myopen2.my_UrlOpen())

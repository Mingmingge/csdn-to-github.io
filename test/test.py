#! /usr/bin/python
# -*- coding: utf-8 -8*-
from utils.imgwriter import ImgWriter
from utils.regcompiler import RegCompiler
from utils.urlopener import MyUrlOpen, MyImgUrlOpen

'''myopen1 = MyUrlOpen('https://blog.csdn.net/babybabyup')
print(myopen1.my_UrlOpen())

myopen2 = MyImgUrlOpen('https://img-blog.csdn.net/20160601100450061?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center')
print(myopen2.my_UrlOpen())

regCompiler = RegCompiler('https://blog.csdn.net/babybabyup/')
i = 0
for key in regCompiler.getArticleUrls():
    print(key)
    i = i+1
print(i)

regCompiler = RegCompiler('https://blog.csdn.net/babybabyup/article/details/79765948')
if regCompiler.getImgUrls():
    for key in regCompiler.getImgUrls():
        print(key)
else:
    print('none')
    '''
imgwriter = ImgWriter('https://img-blog.csdn.net/20180331095106918?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhYnliYWJ5dXA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70','/Users/hulimin/Desktop/789')
imgwriter.imgwrite()


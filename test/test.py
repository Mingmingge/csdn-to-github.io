#! /usr/bin/python
# -*- coding: utf-8 -8*-
import gzip
import io
from utils.articlewriter import ArticleWriter
from utils.hosttourl import hostTourl
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
    
imgwriter = ImgWriter('https://img-blog.csdn.net/20180331095106918?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhYnliYWJ5dXA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70','/Users/hulimin/Desktop/789')
imgwriter.imgwrite()


parenpath = '/Users/hulimin/Desktop/1234'
opener = MyUrlOpen('https://blog.csdn.net/babybabyup/article/list/2')
context = opener.my_UrlOpen()
regcompiler = RegCompiler(context)
i = 0
for key in regcompiler.getArticleUrls():
    print(key)
    articleopener = MyUrlOpen('https://blog.csdn.net/babybabyup/article/details/79815118')
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
    i = i+1
print(i)



parenpath = '/Users/hulimin/Desktop/1234'
opener = MyUrlOpen('https://blog.csdn.net/babybabyup/article/list/2')
context = opener.my_UrlOpen()
regcompiler = RegCompiler(context)
articleopener = MyUrlOpen('https://blog.csdn.net/babybabyup/article/details/79820980')
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


parenpath = '/Users/hulimin/Desktop/1234'
host = 'https://blog.csdn.net/babybabyup'
opener = MyUrlOpen(hostTourl(host,1))
context = opener.my_UrlOpen()
regcompiler = RegCompiler(context)
i = 0
if not regcompiler.getArticleUrls():
    print('none')
for key in regcompiler.getArticleUrls():
    print(key)
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
    i = i+1
print(i)

parenpath = '/Users/hulimin/Desktop/1234'
host = 'https://blog.csdn.net/babybabyup'
i = 1
while 1:
    opener= MyUrlOpen(hostTourl(host, i))
    context = opener.my_UrlOpen()
    regcompiler = RegCompiler(context)
    if regcompiler.getArticleUrls():
        for key in regcompiler.getArticleUrls():
            print(key)
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
        break
    i = i+1
'''

import codecs
import sys

import tomd




save_file = '/Users/hulimin/Desktop/markdown.md'


def run():
    html = getHtml()
    #print(html)
    mdTxt = tomd.Tomd(html).markdown
    print('markdown :{}'.format(mdTxt))



def getHtml():
    return u'''
<div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog"  data-mod=popu_307  data-dsm = "post" >
                    <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-e2445db1a8.css" />
						<div class="htmledit_views">
                
<h1 class="entry-title" style="border:0px;font-style:inherit;font-variant:inherit;line-height:1.2em;font-family:'PT Serif', Georgia, 'Helvetica Neue', Arial, sans-serif;font-size:2.6em;vertical-align:baseline;">
Jdbc 连接 Mysql 时的中文乱码问题</h1>
<p class="meta" style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:'PT Sans', 'Helvetica Neue', Arial, sans-serif;font-size:.9em;vertical-align:baseline;color:rgb(170,170,170);text-transform:uppercase;">
</p>
<div class="entry-content" style="border:0px;line-height:inherit;font-family:'PT Serif', Georgia, Times, 'Times New Roman', serif;font-size:18.4px;vertical-align:baseline;color:rgb(34,34,34);background-color:rgb(248,248,248);">
<p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
本文转载自http://chenyufei.info/blog/2007-06-27/post-070627-095625-802/</p>
<p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
在用 jdbc 向 mysql 数据库插入中文时出现了乱码，严格来说是通过 Hibernate。记录下搜索和查文档以后找到的解决办法。</p>
<ul style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"><li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
首先要告诉数据库要插入的字符串使用的字符集，mysql 默认使用的字符集是 latin1。我要保存的字符串是 UTF-8 编码的（字符集是 Unicode），所以包含这个字段的表应该使用 UTF-8 编码。这里有几种解决办法。
<ol style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"><li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
在建立数据库的时候指定数据库的字符集编码，这样，这个数据库的所有表都会默认使用数据库的字符集编码。如 <code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">create
 database foo charset utf8;</code></li><li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
在建表的时候指定字符集编码。如 <code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">create
 table foo (id char(20)) charset utf8;</code></li><li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
指定某一列使用的字符集编码。如<code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">create
 table foo (id char(20) charset utf8);</code></li></ol>
如果你有需要的话还可以指定字符排序的规则，也就是指定 collation，如 <code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">create
 database foo charset utf8 collate utf8_general_ci;</code>，同样也可以指定单独的表、列使用的 collation 规则。</li><li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
然后在使用 jdbc 连接数据库的时候要告知 jdbc 使用什么字符集编码来跟服务器通信。很简单，只需要在 jdbc 指定数据库路径时做一点修改就可以了。比如，<code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">jdbc:mysql://localhost/test?useUnicode=true&amp;characterEncoding=utf8</code>。注意如果在
 XML 文件里面的话 “&amp;” 要改成 “&amp;”。</li></ul><p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
如果你使用的是 gbk 编码的话把上面所有提到 utf8 的地方改成 gbk 应该就可以了，只要服务器和客户端使用的字符集编码统一就可以了。</p>
<p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
mysql 命令行客户端默认使用的字符集也是 latin1，如果你通过这个来插入中文的话也会出现乱码的情况。解决的办法是执行语句 <code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">set
 names ‘utf8’</code> 来告诉服务器使用 UTF-8 编码来和客户端通信。你也可以使用 <code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">set
 charset ‘utf8’</code>，它和 set names 区别只在于 collation 上。set names 和 set charset 都相当于执行了三条语句，具体的内容可以去看 mysql 文档 10.4 节。我想这个方法在使用 jdbc 的时候也是可以的，所以如果 jdbc 的指定数据库地址中没有告知使用的字符集编码的话可以通过执行上面的语句来达到相同的效果。</p>
<p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
（如果对文章中字符集和字符集编码的使用感到困惑的话去看点 Unicode 方面的文章吧。）</p>
</div>
            </div>
                </div>
    '''

run()




#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import warnings
import bs4

MARKDOWN = {
    'h1': ('\n# ', '\n'),
    'h2': ('\n## ', '\n'),
    'h3': ('\n### ', '\n'),
    'h4': ('\n#### ', '\n'),
    'h5': ('\n##### ', '\n'),
    'h6': ('\n###### ', '\n'),
    'em': ('*', '*'),
    'strong': ('**', '**'),
    'b': ('**', '**'),
    'i': ('*', '*'),
    'code': ('`', '`'),
    'pre': ('\n```\n', '\n```\n'),
    'td': ('|', ''),
    'th': ('|', ''),
    'tr': ('', '\n'),
    'table': ('', '\n'),
    'ul': ('', ''),
    'ol': ('', ''),
    'li': ('\n -  ', '\n'),
    'blockquote': ('\n> ', '\n'),
    'block_code': ('\n```\n', '\n```\n'),
    'span': (' ', '\n'),
    'p': ('\n', '\n'),
    'inline_p': ('', ''),
    'inline_p_with_out_class': ('', ''),
    'del': ('~~', '~~'),
    'hr': ('\n---', '\n\n'),
    'thead': ('\n', '|------\n'),
    'tbody': ('\n', '\n'),
    'e_p': ('', '\n'),
    'img': ('\n![](', ')\n')

}
HTML = {
    'h1': ('<h1.*?>', '</h1>'),
    'h2': ('<h2.*?>', '</h2>'),
    'h3': ('<h3.*?>', '</h3>'),
    'h4': ('<h4.*?>', '</h4>'),
    'h5': ('<h5.*?>', '</h5>'),
    'h6': ('<h6.*?>', '</h6>'),
    'hr': ('<hr.*?', '<hr/>'),
    'blockquote': ('<blockquote.*?>', '</blockquote>'),
    'ul': ('<ul.*?>', '</ul>'),
    'ol': ('<ol.*?>', '</ol>'),
    'li': ('<li>*?>', '</li>'),
    'block_code': ('<pre.*?><code.*?>', '</code></pre>'),
    'p': ('<p.*?>', '</p>'),
    'p_with_out_class': ('<p>', '</p>'),
    'thead': ('<thead.*?>', '</thead>'),
    'tr': ('<tr.*?>', '</tr>'),
    'td': ('<td.*?>', '</td>'),
    'th': ('<th.*?>', '</th>'),
    'b': ('<b.*?>', '</b>'),
    'i': ('<i.*?>', '</i>'),
    'del':('<del.*?>', '</del>'),
    'a': ('<a.*?href="(.*?)".*?>', '</a>'),
    'em': ('<em.*?>', '</em>'),
    'strong':('<strong.*?>', '<strong>')

}
'''BlOCK_ELEMENTS = {
    'h1': '<h1.*?>(.*?)</h1>',
    'h2': '<h2.*?>(.*?)</h2>',
    'h3': '<h3.*?>(.*?)</h3>',
    'h4': '<h4.*?>(.*?)</h4>',
    'h5': '<h5.*?>(.*?)</h5>',
    'h6': '<h6.*?>(.*?)</h6>',
    'hr': '<hr/>',
    'blockquote': '<blockquote.*?>(.*?)</blockquote>',
    'ul': '<ul.*?>(.*?)</ul>',
    'ol': '<ol.*?>(.*?)</ol>',
    'li': '<li.*?>(.*?)<li>',
    'block_code': '<pre.*?><code.*?>(.*?)</code></pre>',
    'p': '<p.*?>(.*?)</p>',
    'p_with_out_class': '<p>(.*?)</p>',
    'thead': '<thead.*?>(.*?)</thead>',
    'tr': '<tr.*?>(.*?)</tr>'
}'''

INLINE_ELEMENT = ['img', 'strong', 'em', 'b', 'code', 'li', 'ul', 'td', 'th', 'tr', 'span']

BLOCK_ELEMENTS = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'pre', 'p']

'''INLINE_ELEMENTS = {
    'strong':'<strong.*?>(.*?)</strong>',
    'em': '<em.*?>(.*?)</em>',
    'b': '<b.*?>(.*?)</b>',
    'code': '<code.*?>(.*?)</code>',
    'td': '<td.*?>((.|\n)*?)</td>',
    'th': '<th.*?>(.*?)</th>',
    'tr': '<tr.*?>((.|\n)*?)</tr>',
    'ul': '<ul.*?>(.*?)</ul>',
    'ol': '<ol.*?>(.*?)</ol>',
    'li': '<li.*?>(.*?)</li>'
    

}'''




'''
'span': '<span.*?>(.*?)</span>',
'i': '<i.*?>(.*?)</i>',
'inline_p_with_out_class': '<p>(.*?)</p>',
'code': '<code.*?>(.*?)</code>',
    'img': '<img.*?src="(.*?)".*?>(.*?)</img>',
    'img_single': '<img.*?src="(.*?)".*?/>',
    'img_single_no_close': '<img.*?src="(.*?)".*?>',
'strong': '<strong.*?>(\s*)(.*?)(\s*)</strong>',
    'tbody': '<tbody.*?>((.|\n)*)</tbody>',
    'a': '<a.*?href="(.*?)".*?>(.*?)</a>',
'''
DELETE_ELEMENTS = ['<span.*?>', '</span>', '<div.*?>', '</div>', '<center.*?>', '</center>', '<link .*?/>','\s', '<br.*?>', '</br>', '<ol.*?>', '</ol>',
                   '<article.*?>', '</article>', '<ul.*?>', '</ul>', '<table.*?>', '</table>', '<thead>']


def deleteElements(context):
    for key in DELETE_ELEMENTS:
        if key == '</span>':
            context = re.sub(key, '\n', context)
        else:
            context = re.sub(key, ' ', context)

    return context


def subElements(context):
    con = context
    soup = bs4.BeautifulSoup(con, 'lxml')
    for ele in INLINE_ELEMENT:
        if soup.find_all(ele):
            for key in soup.find_all(ele):
                print(str(key))
                #con = re.sub(str(key), str(MARKDOWN[ele][0] + str(key.string) + MARKDOWN[ele][1]), con)
                if ele == 'code':
                    if re.search(r'<code style=.*?>.*?</code>', str(key)):
                        con = con.replace(str(key), str(MARKDOWN[ele][0] + str(key.string).strip() + MARKDOWN[ele][1]))
                    else:
                        con = con.replace(str(key), str(key.string))
                elif ele == 'img':
                    print(key)
                    imgpath = os.path.join('../images/',str(os.path.join(re.search(r'\d{10,20}', str(key)).group()) + '.png'))
                    con = con.replace(str(key),str(MARKDOWN[ele][0] + str(imgpath).strip() + MARKDOWN[ele][1]))
                else:
                    con = con.replace(str(key).strip(),str(MARKDOWN[ele][0] + str(key.string).strip() + MARKDOWN[ele][1]))
        else:
            continue
        for ele in BLOCK_ELEMENTS:
            soup = bs4.BeautifulSoup(con, 'lxml')
            if soup.find_all(ele):
                for key in soup.find_all(ele):
                    print(key)
                    con = con.replace(str(key), str(MARKDOWN[ele][0] + str(key.string).strip() + MARKDOWN[ele][1]))
            else:
                continue

    #print(bs4.BeautifulSoup(con, 'lxml').prettify())

    return con







html = """
<article> 
   <div id="article_content" class="article_content clearfix csdn-tracking-statistics" data-pid="blog" data-mod="popu_307" data-dsm="post"> 
    <link rel="stylesheet" href="https://csdnimg.cn/release/phoenix/template/css/ck_htmledit_views-e2445db1a8.css" /> 
    <div class="htmledit_views"> 
    <h2>sdvefvev</h2>
     <h1 class="entry-title" style="border:0px;font-style:inherit;font-variant:inherit;line-height:1.2em;font-family:'PT Serif', Georgia, 'Helvetica Neue', Arial, sans-serif;font-size:2.6em;vertical-align:baseline;"> Jdbc 连接 Mysql 时的中文乱码问题</h1> 
     <p class="meta" style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:'PT Sans', 'Helvetica Neue', Arial, sans-serif;font-size:.9em;vertical-align:baseline;color:rgb(170,170,170);text-transform:uppercase;"> </p> 
     <div class="entry-content" style="border:0px;line-height:inherit;font-family:'PT Serif', Georgia, Times, 'Times New Roman', serif;font-size:18.4px;vertical-align:baseline;color:rgb(34,34,34);background-color:rgb(248,248,248);"> 
      <p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 本文转载自http://chenyufei.info/blog/2007-06-27/post-070627-095625-802/</p> 
      <p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 在用 jdbc 向 mysql 数据库插入中文时出现了乱码，严格来说是通过 Hibernate。记录下搜索和查文档以后找到的解决办法。</p> 
      <ul style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
       <li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 首先要告诉数据库要插入的字符串使用的字符集，mysql 默认使用的字符集是 latin1。我要保存的字符串是 UTF-8 编码的（字符集是 Unicode），所以包含这个字段的表应该使用 UTF-8 编码。这里有几种解决办法。</li> 
        <ol style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;">
         <li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 在建立数据库的时候指定数据库的字符集编码，这样，这个数据库的所有表都会默认使用数据库的字符集编码。如&nbsp;create database foo charset utf8;</li>
         <li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 在建表的时候指定字符集编码。如&nbsp;<code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">create table foo (id char(20)) charset utf8;</code> </li>
         <li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 指定某一列使用的字符集编码。如<code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">create table foo (id char(20) charset utf8);</code> </li>
        </ol> 如果你有需要的话还可以指定字符排序的规则，也就是指定 collation，如&nbsp;<code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">create database foo charset utf8 collate utf8_general_ci;</code>，同样也可以指定单独的表、列使用的 collation 规则。</li>
       <li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 然后在使用 jdbc 连接数据库的时候要告知 jdbc 使用什么字符集编码来跟服务器通信。很简单，只需要在 jdbc 指定数据库路径时做一点修改就可以了。比如，<code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">jdbc:mysql://localhost/test?useUnicode=true&amp;characterEncoding=utf8</code>。注意如果在 XML 文件里面的话 “&amp;” 要改成 “&amp;”。</li>
      </ul>
      <p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 如果你使用的是 gbk 编码的话把上面所有提到 utf8 的地方改成 gbk 应该就可以了，只要服务器和客户端使用的字符集编码统一就可以了。</p> 
      <p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> mysql 命令行客户端默认使用的字符集也是 latin1，如果你通过这个来插入中文的话也会出现乱码的情况。解决的办法是执行语句&nbsp;<code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">set names ‘utf8’</code>&nbsp;来告诉服务器使用 UTF-8 编码来和客户端通信。你也可以使用&nbsp;<code style="border:1px solid rgb(221,221,221);font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:1.5em;font-family:Menlo, Monaco, 'Andale Mono', 'lucida console', 'Courier New', monospace;font-size:.8em;vertical-align:baseline;display:inline-block;background:rgb(255,255,255);color:rgb(85,85,85);">set charset ‘utf8’</code>，它和 set names 区别只在于 collation 上。set names 和 set charset 都相当于执行了三条语句，具体的内容可以去看 mysql 文档 10.4 节。我想这个方法在使用 jdbc 的时候也是可以的，所以如果 jdbc 的指定数据库地址中没有告知使用的字符集编码的话可以通过执行上面的语句来达到相同的效果。</p> 
      <p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> （如果对文章中字符集和字符集编码的使用感到困惑的话去看点 Unicode 方面的文章吧。）</p> 
     </div> 
    </div> 
   </div>
   <pre class="prettyprint"><code class=" hljs bash">! /bin/bash
<span class="hljs-built_in">read</span> -t <span class="hljs-number">10</span> -p <span class="hljs-string">"请输入您的姓名：  "</span> name
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$name</span>

<span class="hljs-built_in">read</span> <span class="hljs-operator">-s</span> pas
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$pas</span>        </code></pre> 
<pre class="prettyprint"><code class=" hljs bash">! /bin/bash
<span class="hljs-built_in">read</span> -t <span class="hljs-number">10</span> -p <span class="hljs-string">"请输入您的姓名：  "</span> name
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$name</span>

<span class="hljs-built_in">read</span> <span class="hljs-operator">-s</span> pas
<span class="hljs-built_in">echo</span> <span class="hljs-variable">$pas</span>        </code></pre> 
<strong>strooo  
</strong>  
  </article>
"""

#print(deleteElements(html))

soup  = bs4.BeautifulSoup(deleteElements(html), 'lxml')
soup1 = bs4.BeautifulSoup(html, 'lxml')
'''print(soup.h1)
for p in soup.find_all('p'):
    print(p)

for code in soup.find_all('code'):
    print(code.string)
for strong in soup.find_all('strong'):
    print(strong.string)
    
    
    
    
    
    
    con = context
    for key in INLINE_ELEMENTS:
        list = re.findall(re.compile(INLINE_ELEMENTS[key]), str(con))
        if not list:
            continue
        else:
            for li in list:
                if 1:
                    subcon = str(MARKDOWN[key][0]) + str(li) + str(MARKDOWN[key][1])
                    try:
                        con = re.sub(HTML[key][0] + str(li) + HTML[key][1], subcon, con)
                    except:
                        print("inline error")
    for key in BlOCK_ELEMENTS:
        list = re.findall(re.compile(BlOCK_ELEMENTS[key]), str(con))
        if not list:
            continue
        else:
            for li in list:
                # print(li)
                subcon = str(MARKDOWN[key][0]) + str(li) + str(MARKDOWN[key][1])
                # print(subcon)
                try:
                    con = re.sub(HTML[key][0] + str(li) + HTML[key][1], subcon, con)
                except:
                    print('block error')
                    continue
                con = re.sub(HTML[key][0] + str(li) + HTML[key][1], subcon, con)
    #print(con)
    return con

    

for key in soup.find_all('li'):
        print(key)'''


#print(soup.pre.contents)
#print(soup.code.contents)

html2 = """# Jdbc 连接 Mysql 时的中文乱码问题
       

                
本文转载自http://chenyufei.info/blog/2007-06-27/post-070627-095625-802/
        
在用 jdbc 向 mysql 数据库插入中文时出现了乱码，严格来说是通过 Hibernate。记录下搜索和查文档以后找到的解决办法。
                 
 -  首先要告诉数据库要插入的字符串使用的字符集，mysql 默认使用的字符集是 latin1。我要保存的字符串是 UTF-8 编码的（字符集是 Unicode），所以包含这个字段的表应该使用 UTF-8 编码。这里有几种解决办法。
                     <li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 在建立数据库的时候指定数据库的字符集编码，这样，这个数据库的所有表都会默认使用数据库的字符集编码。如&nbsp;create database foo charset utf8;</li>          <li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 在建表的时候指定字符集编码。如&nbsp;`create table foo (id char(20)) charset utf8;` </li>          
 -  指定某一列使用的字符集编码。如`create table foo (id char(20) charset utf8);`
           如果你有需要的话还可以指定字符排序的规则，也就是指定 collation，如&nbsp;`create database foo charset utf8 collate utf8_general_ci;`，同样也可以指定单独的表、列使用的 collation 规则。</li>        <li style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> 然后在使用 jdbc 连接数据库的时候要告知 jdbc 使用什么字符集编码来跟服务器通信。很简单，只需要在 jdbc 指定数据库路径时做一点修改就可以了。比如，`jdbc:mysql://localhost/test?useUnicode=true&characterEncoding=utf8`。注意如果在 XML 文件里面的话 “&amp;” 要改成 “&amp;”。</li>               
如果你使用的是 gbk 编码的话把上面所有提到 utf8 的地方改成 gbk 应该就可以了，只要服务器和客户端使用的字符集编码统一就可以了。
        <p style="border:0px;font-style:inherit;font-variant:inherit;font-weight:inherit;line-height:inherit;font-family:inherit;font-size:18.4px;vertical-align:baseline;"> mysql 命令行客户端默认使用的字符集也是 latin1，如果你通过这个来插入中文的话也会出现乱码的情况。解决的办法是执行语句&nbsp;`set names ‘utf8’`&nbsp;来告诉服务器使用 UTF-8 编码来和客户端通信。你也可以使用&nbsp;`set charset ‘utf8’`，它和 set names 区别只在于 collation 上。set names 和 set charset 都相当于执行了三条语句，具体的内容可以去看 mysql 文档 10.4 节。我想这个方法在使用 jdbc 的时候也是可以的，所以如果 jdbc 的指定数据库地址中没有告知使用的字符集编码的话可以通过执行上面的语句来达到相同的效果。</p>        
（如果对文章中字符集和字符集编码的使用感到困惑的话去看点 Unicode 方面的文章吧。）
                         
```
! /bin/bash  read  -t  10  -p  "请输入您的姓名：  "  name  echo   $name    read   -s  pas  echo   $pas
```
  **strooo**       """


html3 = """
<p>最后，安装验证代码正确性啦，   <img src="https://img-blog.csdn.net/20180603132405509?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhYnliYWJ5dXA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="" title="">   以及卸载模块后：   <img src="https://img-blog.csdn.net/2018060313235489?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhYnliYWJ5dXA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="" title=""></p> """
soup3 = bs4.BeautifulSoup(html3, 'lxml')
#for key in soup3.find_all('img'):
    #if re.search(r'\d{10,20}', str(key)):
        #print(os.path.join('../images/', str(os.path.join(re.search(r'\d{10,20}', str(key)).group())+'.png')))
with open('/Users/hulimin/Desktop/1.md' ,'w') as file:
    file.write(subElements(deleteElements(html3)))




#! /usr/bin/python
# -*- coding: utf-8 -*

import re
from utils import urlopener


myopen1 = urlopener.MyUrlOpen('https://blog.csdn.net/babybabyup')
fullcontext = myopen1.my_UrlOpen()
#print(myopen1.my_UrlOpen())
contextObj = re.search('meta', str(fullcontext), re.M|re.I)
if contextObj:
    contextObj.group()
else:
    print('none')


#! /usr/bin/python
# -*- coding: utf-8 -*-
import os

import re

from utils.regcompiler import RegCompiler


class ArticleWriter(object):

    def __init__(self, context, title, parentpath) -> None:
        super().__init__()
        self.fullcontext = context
        self.title = title
        self.parentpath = parentpath

    def articlewrite(self):
        if not os.path.exists(self.parentpath):
            os.mkdir(self.parentpath)
        path = os.path.join(self.parentpath,'articles')
        if not os.path.exists(path):
            os.mkdir(path)
        articlename = os.path.join(path, self.title+'.md')
        try:
            with open(articlename, 'w') as file:
                file.write(self.fullcontext)
        except:
            print("文件写入错误！")


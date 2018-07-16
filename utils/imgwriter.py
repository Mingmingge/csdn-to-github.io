#! /usr/bin/python
# -*- coding: utf-8 -*-


from os import path
import os
import re
from utils import urlopener


class ImgWriter(object):

    def __init__(self, url, parentpath) -> None:
        super().__init__()
        self.url = url
        self.parentpath = parentpath

    def imgwrite(self):
        if not path.exists(self.parentpath):
            os.mkdir(self.parentpath)
        imgname = re.search(r'\d{10,20}', self.url).group()
        imgpath = path.join(self.parentpath, imgname+'.png')
        myopen = urlopener.MyImgUrlOpen(self.url)
        try:
            with open(imgpath, 'wb') as file:
                file.write(myopen.my_UrlOpen())
        except:
            print('图片写入错误！')


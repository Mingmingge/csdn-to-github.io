#! /usr/bin/python
# -*- coding: utf-8 -*-
import os


def hostTourl( host, i):
    url = os.path.join(host, 'article/list/' + str(i))
    return url
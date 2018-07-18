#! /usr/bin/python
# -*- coding: utf-8 -*-


list = ['1', '2', '3', '4', '5', '6']
for key in list:
    print(key)


set = set(list)
for key in set:
    print(key)
dict  = {
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6'

}

for key in dict:
    print(key)



str = "this is" \
      "string example....wow!!! this is really string"
print(str.replace("is", "was"))
print (str.replace("is", "was", 3))
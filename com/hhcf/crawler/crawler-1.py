#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@version: 1.0
@author: zhaotf
@file: crawler-1.py
@time: 2017/8/7 0007 10:22
"""


# 网页 http://blog.csdn.net/fly_yr/article/details/51525435
import urllib.request

# 网址
url = "http://www.douban.com/"
# 请求
request = urllib.request.Request(url)
# 爬取结果
response = urllib.request.urlopen(request)
data = response.read()
# 设置解码方式
data = data.decode("utf-8")
# 打印结果
print(data)
# 打印爬取网页信息
print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())



def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

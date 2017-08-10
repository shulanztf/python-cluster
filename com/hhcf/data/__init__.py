#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
python 文件读取
@version: 1.0
@author: zhaotf
@file: __init__.py.py
@time: 2017/8/10 0010 10:00
"""
import pandas

reader = pandas.read_csv('D:\servicelog.csv', iterator=True)
try:
    df = reader.get_chunk(100 * 1000 * 1000)
    # print(df)
    # print(df.tail(10))
    # print(df.head(15))
    # print(df.items)
    # print(df.)


except StopIteration as si:
    print("重复ection")
finally:
    print("最终出口")



def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

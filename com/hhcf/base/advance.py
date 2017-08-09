#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@version: 1.0
@author: zhaotf
@file: advance.py
@time: 2017/8/9 0009 16:59
"""

list1 = ['aaa', 'bb', 'cc', 'dddddddddd']
# 从索引0开始取，直到索引3为止，但不包括索引3
print(list1[0:3])
print(list1[:3])
# 倒数第一个元素的索引是-1
print(list1[-2:])

try:
    print(list1[8])
except Exception as e:
    print("异常发生", e)
except BaseException as e:
    print("汇总异常", e)
finally:
    print("最终出口")







def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

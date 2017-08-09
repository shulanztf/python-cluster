#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@version: 1.0
@author: zhaotf
@file: __init__.py.py
@time: 2017/8/7 0007 15:18
"""

# python 函数定义、可变参数

# def func():
#     pass
# # func()

# def funcB(aa, bb):
#     print(aa)
#     print(bb)
# funcB(33,'cc')

# 不定参数
def funcD(aa, bb, *c):
    print(aa)
    print(bb)
    print("长度 ：" , len(c))
    print(c)
    print(len(c))

funcD(11,32,59,33)
funcD(11,32,"acb323")
funcD(11,32,"acb323",3525)



class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

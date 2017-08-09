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

# 不定长参数
# def funcD(aa, bb, *c):
#     print(aa)
#     print(bb)
#     print("长度 ：" , len(c))
#     print(c)
#     print(len(c))
#
# funcD(11,32,59,33)
# funcD(11,32,"acb323")
# funcD(11,32,"acb323",3525)

# # 可写函数
# def funcF(arg1, arg2):
#     print(arg1)
#     print(arg2)
#     return
# # 调用
# funcF(arg1="abc", arg2=33)
# funcF(arg2=33, arg1="abc")

# # 默认函数
# def funcG(arg1,arg2=33):
#     print(arg1)
#     print(arg2)
# funcG("abc")
# funcG("qwe", 98)

# # 匿名函数、可写函数
# funcSum = lambda arg1, arg2: arg1 - arg2
# print("调用 匿名：",funcSum(3,15))

# # 全局变量、局部变量
# tal = 0
# def funcH(arg1):
#     print("局部变量：",tal)
#
# print("全局变量：",tal)
# funcH()

class Province():
    # 静态字段
    country = "中国"

    def __init__(self,name):
        # 普通字段
        self.name = name

    def res(self):
        return self.name

    def __str__(self):
        return "这是类class"

    def prt(self):
        print("eeee:", self)
        print("ddddd:", self.__class__)


# 直接访问普通字段
obj = Province("山东")
obj.prt()
Province.prt(obj)
print("自定义类：", obj.name)
print("ccc:", obj.__str__())
# 访问静态字段
print("静态字段：", Province.country)
print("aaa:", obj.res())

if __name__ == '__main__':
    pass

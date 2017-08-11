#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@version: 1.0
@author: zhaotf
@file: __init__.py.py
@time: 2017/8/7 0007 10:22
"""

class Sample:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("type:", exc_type)
        print("value:", exc_val)
        print("trace:", exc_tb)

    def do_someth(self):
        bra = 1/0
        return bra + 32

with Sample() as sam:
    sam.do_someth()

# # 闭包
# def makeB(fun):
#     def wrap():
#         return "ztf:" + fun()
#     return wrap()
#
# @makeB
# def hel():
#     return "azxgefe4"
#
# print(hel())
# print(makeB(hel))


# avb = {'aa':'a3ed','bb':'23','cc':'15'}
# print(type(avb))
# print(len(avb))













# import easygui
#
# msg = easygui.msgbox("aasaacc")
# title = easygui.msgbox(msg="mw内容",title="剽一",ok_button="确定1")

# numbers = [1,2,3,4,5,6,7,8,9,0,11,16]
# numbers = ["12dd","dw3","ave33","23","abc"]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(numbers[0:10:1])
# print([1,2,3] + [4,5,6])

# var1 = "abcedw"
# var2 = "aeiwon2323jjjj"
# print("abcedw"[3])
# var3 = "aaa %s ade %s ewew %s eew  ew"
# print(var3 % ("砂", "仍", 33))

# print("vsar1[0]:", var1)
# print("vsar1[0]:", var1[0])
# print("var2[1:5]:", var2)
# print("var2[1:5]:", var2[1:5])
# print(var1 * 3)

# obj = 520.3
# print(type(obj))
#
# print(isinstance(obj, str))
# print(isinstance(obj, int))
# print(isinstance(obj, float))






def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

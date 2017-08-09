#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@version: 1.0
@author: zhaotf
@file: super-1.py
@time: 2017/8/9 0009 16:07
"""

# 继承多态
class Animal(object):
    def __init__(self):
        pass

    def run(self, text):
        print("基类", text, object)

class Dag(Animal):

    def run(self, text):
        print("dao:", text)

    def eat(self):
        print("dao eat:")

class Cat(Animal):

    def run(self, text):
        print("cat:", text)

    def eat(self):
        print("cat eat:")

dog1 = Dag()
dog1.run("汪")

cat1 = Cat()
cat1.run("喵")

print(type(dog1))
print(type(cat1))

print(isinstance(dog1, Dag))
print(isinstance(cat1, Cat))
print(isinstance(cat1, Dag))
print(isinstance(cat1, Animal))

if __name__ == '__main__':
    pass

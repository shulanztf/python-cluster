#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@version: 1.0
@author: zhaotf
@file: pyplot1.py
@time: 2017/8/10 0010 13:50
"""
# Import necessary packages

import matplotlib
import numpy
# from numpy  import array
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
DataX =[1,2,3,4,5,6,7]
DataY =[7,6,5,4,3,2,1]
ax.scatter(DataX,DataY,15.0* numpy.array(DataX),15.0* numpy.array(DataY))
plt.show()

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

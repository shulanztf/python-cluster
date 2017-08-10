#! /usr/bin/env python
# -*- encoding: utf-8 -*-
"""
GDP图形展示
http://www.cnblogs.com/vamei/archive/2012/09/17/2689798.html
@version: 1.0
@author: zhaotf
@file: major_country_gdp.py
@time: 2017/8/10 0010 11:12
"""

import matplotlib
import pylab

labels = []
quants = []
# file = open("D:\\workspace\python-cluster\com\hhcf\view\major_country_gdp.txt", 'r')
file = open(".\major_country_gdp.txt", 'r')
for line in file:
    info = line.split()
    labels.append(info[0])
    quants.append(float(info[1]))

pylab.figure(1, figsize=(6, 6))


def explode(label, target='China'):
    if label == target:
        return 0.1
    else:
        return 0


expl = map(explode, labels)
colors = ["pink", "coral", "yellow", "orange"]

pylab.pie(quants, expl, colors=colors, labels=labels, autopct="%1.1f%%", pctdistance=0.8, shadow=True)
pylab.title("TOP 10 gdp中", bbox={'facecolor': '0.8', 'pad': 5})

pylab.show()


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass

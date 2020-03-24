"""

"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from sklearn.neighbors import KDTree

"""
文件读取处理
returnMat:特征矩阵
classLabelVector:类别号向量
"""
def file2matrix(filename):
    fr =open(filename)
    arrayOflines = fr.readlines() # readlines:是一次性将这个文本的内容全部加载到内存中(列表)
    numOfLines = len(arrayOflines) # 获取文件行数
    returnMat = np.zeros((numOfLines,2)) # 创建numOfLines*3的0矩阵，存储特征数据
    classLabelVector = [] # 存储最后一列，类别号
    index = 0
    for line in arrayOflines:
        # print("eclipse:",line) # 异常数据打印
        line = line.strip()
        # print(line.split("\t"))
        listFromline = list(map(float,line.split("\t"))) # 批量转换，并类型转换(list)，str->float
        returnMat[index,:] = listFromline[2:4] # 取前3列
        classLabelVector.append(int(listFromline[-1])) # 取最后一列
        index += 1
    return returnMat, classLabelVector



if __name__ == '__main__':
    # np.random.seed(0)
    # points = np.random.random((100, 2))
    points,labels = file2matrix("D:\data\hlht\point\points-data-label\\points-label-train-20200319.txt")
    print(points.shape)
    tree = KDTree(points)
    print(tree) # 数据显示
    point = points[0]
    # kNN
    dists, indices = tree.query([point], k=3)
    # print(dists, indices) # 数据显示
    # query radius
    indices = tree.query_radius([point], r=0.2)
    # print(indices) # 数据显示
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.add_patch(Circle(point, 0.2, color='r', fill=False))
    X, Y = [p[0] for p in points], [p[1] for p in points]
    plt.scatter(X, Y)
    plt.scatter([point[0]], [point[1]], c='r')
    plt.show()

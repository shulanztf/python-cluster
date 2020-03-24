"""
https://leileiluoluo.com/posts/kdtree-algorithm-and-implementation.html k-d tree算法原理及实现
scikit-learn是一个实用的机器学习类库，其有KDTree的实现。
如下例子为直观展示，仅构建了一个二维空间的k-d tree，然后对其作k近邻搜索及指定半径的范围搜索。
多维空间的检索，调用方式与此例相差无多
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from sklearn.neighbors import KDTree

# 测试数据
np.random.seed(0)
points = np.random.random((100, 2))

# print(points) # 数据显示
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


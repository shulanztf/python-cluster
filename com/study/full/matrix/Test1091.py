"""
https://mp.weixin.qq.com/s/G5su9P4IaiHYD58nZ9V8Sw
第 109 天：NumPy 矩阵
"""

# (1) 定义一个3 X 3的矩阵，数据类型为 int
import numpy as np


# (1) 定义一个3 X 3的矩阵，数据类型为 int
# data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# A = np.mat(data, int)
# print(A, type(A))

# (2) 定义一个3 X 3的矩阵，矩阵元素全为0，数据类型为 int
# a = np.mat(np.zeros((3,3)), int)
# print(a)

# (3) 定义一个3 X 3的矩阵，矩阵元素全为1
# a = np.mat(np.ones((3,3)))
# print(a)

# (4) 定义一个3 X 3的单位矩阵
# a = np.mat(np.eye(3,3),int)
# print(a)

# (5) 定义一个3 X 3的对角矩阵，主对角线之外的元素皆为0
# a = np.mat(np.diag([1,2,3]),int)
# print(a)

# (6) 定义一个3 X 3的矩阵，把100作为所有元素初始值
a = np.mat(np.full((3,3),100),int)
print(a)


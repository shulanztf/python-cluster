"""
https://mp.weixin.qq.com/s/G5su9P4IaiHYD58nZ9V8Sw
第 109 天：NumPy 矩阵
"""

# (1) 定义一个3 X 3的矩阵，数据类型为 int
import numpy as np

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A = np.mat(data, int)
print(A, type(A))

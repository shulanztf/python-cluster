"""
https://mp.weixin.qq.com/s/G5su9P4IaiHYD58nZ9V8Sw
"""
import  numpy as np

# 2.1 矩阵的加法与减法
# 只有两个矩阵的行数和列数相等时，才可以进行矩阵的加法和减法运算，否则程序会抛出 ValueError 异常。
# a = np.mat(np.full((3,3),100),int)
# b = np.mat(np.full((3,3),200),int)
# print(a)
# print(b)
# print("----------")
# print(a+b)
# print(a-b)

# 2.2 矩阵的数乘
# 某个实数乘以矩阵称作矩阵的数乘。
# a = 0.1
# b = np.mat(np.full((3,3),100),int)
# print(a*b)

# 2.3 矩阵的点乘
# 只有在第一个矩阵的列数与第二个矩阵的行数相等时，两个矩阵才能相乘，否则程序会抛出 ValueError 异常。
# a = np.mat(np.full((2,3),10),int)
# b = np.mat(np.full((3,3),10),int)
# print(a*b) # 求矩阵相乘形式一
# print(a.dot(b)) # 求矩阵相乘形式二
# print(np.dot(a,b)) # 求矩阵相乘形式三

# 2.4 矩阵的转置
# 把矩阵的每一行转换为列，称为矩阵的转置。
# data = [[1,2,3],[4,5,6],[7,8,9]]
# a = np.mat(data,int)
# print(a.T)

# 2.5 矩阵的求逆
# 非奇异矩阵下，可以对矩阵进行求逆运算。(非奇异矩阵就是行列式不为 0 的矩阵)
# data = [[1,2],[3,4]]
# a = np.mat(data,int)
# print(a.I)

# 2.6 矩阵的行列式
# 对于矩阵 A，均可对应一个标量 det(A)，它的值将告诉我们矩阵是否为非奇异的。
# 计算结果不等于-2，是因为浮点数运算存在精度损失。
# a = np.mat([[1,2],[3,4]], int)
# det = np.linalg.det(a)
# print(det)

# 2.7 矩阵的秩
# 如果把矩阵看成一个向量组，那么秩就是线性无关向量的个数，也就是向量组的维度，概念比较复杂，有兴趣的读者可以继续探索。矩阵的秩应该是小于等于行数与列数的最小值。
# a = np.mat([[1,2],[3,4]],int)
# rank = np.linalg.matrix_rank(a)
# print(rank)

# 2.8 矩阵特征值和特征向量
# A 为 n 阶矩阵，若数 λ 和 n 维非0列向量 x 满足 Ax=λx，那么数 λ 称为 A 的特征值，x 称为 A 的对应于特征值 λ的特征向量。
# 求矩阵 A 的特征值和其对应的特征向量
# a = np.mat([[1,2],[3,4]],int)
# value, vector = np.linalg.eig(a)
# print(value)
# print(vector)

# 2.9 矩阵的线性方程解
# 求解形如 Ax = b 的线性方程组，其中 A 为矩阵，b 为一维或二维的数组，x 是未知变量。
# 求解如下线性方程组的解：
# x + y + z = 3
# 3x + y + 4z = 8
# 8x + 9y + 5z = 22
a = np.mat([[1,1,1],[3,1,4],[8,9,5]],int)
b = np.mat([[3],[8],[22]],int)
x = np.linalg.solve(a,b)
print(x)


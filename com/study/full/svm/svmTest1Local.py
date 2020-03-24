"""
https://blog.csdn.net/sinat_34072381/article/details/84076568 支持向量机SVM（五）：SVC之python实现

"""
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy import *


class Kernel:

    @staticmethod
    def linear():
        return lambda x, y: float(inner(x, y))

    @staticmethod
    def gaussian(sigma):
        return lambda x, y: exp(
            float(linalg.norm(x - y)) ** 2 / (-2 * sigma ** 2))

    @staticmethod
    def _polykernel(dimension, offset):
        return lambda x, y: (offset + float(inner(x, y))) ** dimension

    @classmethod
    def inhomogenous_polynomial(cls, dimension):
        return cls._polykernel(dimension=dimension, offset=1.0)


class SVC:

    def __init__(self, kernel, C=0.5, max_iter=100, eps=1e-3):
        """
        构造函数
        :param kernel: 核函数指针
        :param C: 惩罚参数
        :param max_iter: 无任何变量改变时的最大迭代次数
        :param eps: KKT条件检验范围（容错率）
        """
        self.C = C
        self.kernel = kernel
        self.max_iter = max_iter
        self.eps = eps

    def fit(self, X, y):
        """
        训练模型
        :param X: 输入特征集, 样本数*特征数
        :param y: 输入标签集, 1*样本数, 类别为+1或-1
        :return: self
        """
        self._X = mat(X, dtype=float64)
        self._Y = mat(y, int8).T
        n_samples, n_features = X.shape

        # 初始化alpha、gram矩阵、误差矩阵
        self._K = self.__gram_matrix(self._X)

        self._E = mat(-self._Y, dtype=float64)
        self._alphas = mat(zeros((n_samples, 1)))
        self.b = 0

        # 是否遍历全部变量
        entire = True

        # 内循环有效更改变量次数
        pair_changed = 0

        for _ in range(self.max_iter):
            # 若已遍历全部变量, 变量未有效更新, 则终止循环
            if not entire and pair_changed == 0:
                break
            pair_changed = 0
            if entire:
                for i in range(n_samples):
                    pair_changed += self.__inner_loop(i)
            else:
                for i in where((self._alphas > 0) & (self._alphas < self.C))[0]:
                    pair_changed += self.__inner_loop(i)

            # 若已遍历全部变量, 则下次一定遍历边界变量;
            # 若已遍历边界变量, 变量得到有效更新，则下次仍遍历边界变量;
            entire = False if entire else pair_changed == 0

        # 计算模型
        sv = where(self._alphas > 0)[0]
        self.sv_X = self._X[sv]
        self.sv_Y = self._Y[sv]
        self.sv_alphas = self._alphas[sv]
        self.w = (multiply(self.sv_alphas, self.sv_Y).T * self.sv_X).T
        return self

    def __inner_loop(self, i):
        """内循环"""
        # 临时变量, 用于减少访问, 加速计算
        alphas, b, C, E, K = self._alphas, self.b, self.C, self._E, self._K

        alphaIold, Yi, Ei = alphas[i, 0], self._Y[i, 0], E[i, 0]
        # 满足KKT条件, 则跳出本次循环
        if not (
                alphaIold < C and Yi * Ei < -self.eps or alphaIold > 0 and Yi
                * Ei > self.eps):
            return 0

        # 选择第二个变量
        j = self.__select_j(i)
        alphaJold, Yj, Ej = alphas[j, 0], self._Y[j, 0], E[j, 0]

        # 计算剪辑边界
        if Yi == Yj:
            L = max(0, alphaJold + alphaIold - C)
            H = min(C, alphaJold + alphaIold)
        else:
            L = max(0, alphaJold - alphaIold)
            H = min(C, C + alphaJold - alphaIold)
        if L == H:
            return 0
        eta = K[i, i] + K[j, j] - 2.0 * K[i, j]
        if eta == 0:
            return 0

        # 更新第二个变量
        unc = alphaJold + Yj * (Ei - Ej) / eta
        alphas[j, 0] = H if unc > H else L if unc < L else unc
        deltaJ = Yj * (alphas[j, 0] - alphaJold)

        # 更新第一个变量
        alphas[i, 0] -= Yi * deltaJ

        # 更新b值
        deltaI = Yi * (alphas[i, 0] - alphaIold)
        b1 = b - Ei - deltaI * K[i, i] - deltaJ * K[i, j]
        b2 = b - Ej - deltaI * K[i, j] - deltaJ * K[j, j]
        if 0 < alphas[i, 0] < C:
            self.b = b1
        elif 0 < alphas[j, 0] < C:
            self.b = b2
        else:
            self.b = 0.5 * (b1 + b2)

        # 更新误差矩阵
        E += ([deltaI, deltaJ] * K[[i, j]]).T + (self.b - b)

        return 1 if abs(deltaJ) > 0.00001 else 0

    def score(self, X, y):
        """
        计算模型预测正确率
        :param X: 输入特征集, m*n
        :param y: 输入标签集, 1*m
        :return: 0~1
        """
        y_ptd = self.predict(X)
        error_nums = len(where(y_ptd != mat(y).T)[0])
        return 1 - error_nums / len(X)

    def predict(self, X):
        """
        预测类别
        :param X: 输入特征集, m*n
        :return: 各样本类别, m*1
        """
        X = mat(X)
        kernel = self.kernel
        sv_X = self.sv_X
        K = mat([[kernel(x, xi) for xi in sv_X] for x in X])
        y = mat([1] * len(X)).T
        y[K * multiply(self.sv_alphas, self.sv_Y) + self.b < 0] = -1
        return y

    def __gram_matrix(self, X):
        """
        计算gram矩阵, 用于加速计算
        :param X: 输入特征集
        :return: gram矩阵
        """
        n_samples, n_features = X.shape
        K = mat(zeros((n_samples, n_samples)))
        # 利用核函数计算内积
        for i, x_i in enumerate(X):
            for j, x_j in enumerate(X[:i + 1]):
                K[i, j] = K[j, i] = self.kernel(x_i, x_j)
        return K

    def __select_j(self, i):
        """
        通过最大化步长的方式来获取第二个alpha值的索引.
        :param i: 第一个变量编号
        :return: 第二个变量编号
        """
        j, E = i, self._E

        # 查找最小误差的变量编号
        if E[i] > 0:
            min_error = inf
            for k in where((self._alphas > 0) & (self._alphas < self.C))[0]:
                if k != i and E[k] < min_error:
                    j, min_error = k, E[k]
        # 查找最大误差的变量编号
        else:
            max_error = -inf
            for k in where((self._alphas > 0) & (self._alphas < self.C))[0]:
                if k != i and E[k] > max_error:
                    j, max_error = k, E[k]
        while j == i:
            j = random.randint(0, self._X.shape[0])
        return j

"""
将训练集中的数据进行归一化
归一化的目的：
    训练集中飞行公里数这一维度中的值是非常大，那么这个纬度值对于最终的计算结果(两点的距离)影响是非常大，
    远远超过其他的两个维度对于最终结果的影响
实际约会姑娘认为这三个特征是同等重要的
下面使用最大最小值归一化的方式将训练集中的数据进行归一化
normDataSet:归一化值矩阵，最小值/最大最小差值
range:最大最小差值向量
minVals:最小值向量
"""
def autoNorm(dataSet):
    #     dataSet.min(0)   代表的是统计这个矩阵中每一列的最小值     返回值是一个矩阵1*3矩阵
    minVals = dataSet.min(0) # 将每列中的最小值，合成一行
    maxVals = dataSet.max(0) # 将每列中的最大值，合成一行
    range = maxVals - minVals # 最大最小值归一化
    m = dataSet.shape[0] # 获取矩阵行数
    #     normDataSet存储归一化后的数据
    # normDataSet = np.zeros(np.shape(dataSet)) # 创建dataSet的对应矩阵，行列数相同，元素全为0
    normDataSet = dataSet - tile(minVals, (m, 1))  # 创建dataSet的对应矩阵，行列数相同，元素为dataSet每列最小值，并与dataSet相减
    tmp1 = tile(range, (m,1))
    print("a3:",range,m,tmp1.shape) # 数据显示
    normDataSet = normDataSet / tile(range, (m,1)) # 创建dataSet的对应矩阵，行列数相同，元素为dataSet最大最小差值，并计算，最小值/最大最小差值
    return normDataSet,range,minVals

if __name__ == '__main__':

    """
    回参1:特征值矩阵
    回参2:类别号向量
    """
    def load_data(filename):
        """读取数据"""
        X, y = [], []
        with open(filename) as f:
            for line in f.read().strip().split('\n'):
                line_array = line.split('\t')
                # print("aaa:",line)
                X.append(line_array[2:])
                # print("abc:",line_array[2:])
                if(int(line_array[0]) == 0):  # 类别号转换
                    y.append("-1")
                else:
                    y.append(line_array[0])
                # print("edf:",line_array[0])
        return array(X, float64), array(y, float64)


    def plot_2Dsvm(X, y, w, b, alphas):
        """显示二维SVM"""
        X, y = array(X), array(y)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # 绘制样本散点图
        colors = array(['g'] * X.shape[0])
        colors[y > 0] = 'b'
        ax.scatter(X[:, 0], X[:, 1], s=30, c=colors, alpha=0.5)

        # w1x+w2y+b=0, 取两点绘制超平面及间隔
        x_min = X[where(X[:, 0] == X[:, 0].min())[0], 0]
        x_max = X[where(X[:, 0] == X[:, 0].max())[0], 0]
        x = array([x_min, x_max])
        y = (- b - w[0, 0] * x) / w[1, 0]
        y1 = (- b - linalg.norm(w, 2) - w[0, 0] * x) / w[1, 0]
        y2 = (- b + linalg.norm(w, 2) - w[0, 0] * x) / w[1, 0]
        print("aaa1:",x)# 数据显示
        print("aaa2:",x.shape)# 数据显示
        print("bbb1:",y)# 数据显示
        print("bbb2:",len(y))# 数据显示
        ax.plot(x, y, 'r')
        ax.plot(x, y1, 'r--', alpha=0.2)
        ax.plot(x, y2, 'r--', alpha=0.2)

        for k in where(alphas > 0)[0]:
            plt.scatter(X[k, 0], X[k, 1], color='', edgecolors='r', marker='o',
                        s=150)
        plt.show()


    X, y = load_data(r"D:\data\hlht\point\points-data-label\\points-label-train-20200324.txt")
    # X, y = load_data(r"D:\data\hlht\point\points-data-label\\points-label-train-20200320.txt")
    # print("a1:",X[:10,:]) # 数据显示
    normMat, ranges, minVals = autoNorm(X)    # 归一化
    # print("a2:",normMat[:10,:]) # 数据显示

    svc = SVC(kernel=Kernel.linear(), C=2)
    # svc = SVC(kernel=Kernel.gaussian(0.6), C=20)
    svc.fit(normMat, y)
    # print("abc:",svc.score(X, y))
    # print("edf:",svc.w)

    plot_2Dsvm(normMat, y, svc.w, svc.b, svc._alphas)





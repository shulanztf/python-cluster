# coding:utf-8
"""
Created on 2020年3月23日
https://blog.csdn.net/NichChen/article/details/85108834 KNN（python实现）
"""

import numpy as np
import operator
import matplotlib.pyplot as plt
from array import array
from matplotlib.font_manager import FontProperties

"""
将每行特征的合计值，计算与其它行距离(欧式距离)，将最近的前k行特征,取频率最高的类别号
normData:测试数据,归一化矩阵的某一行
dataSet:训练数据,归一化矩阵的部分行
labels:归一化矩阵的部分行，对应的类别号向量
k:k值
"""
def classify(normData, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] #获取矩阵的行数
    diffMat = np.tile(normData, (dataSetSize,1)) - dataSet # 创建dataSet对应的矩阵，内容为normData行，并与dataSet相减
    sqDiffMat = diffMat ** 2 # diffMat矩阵开平方
    sqDistances = sqDiffMat.sum(axis = 1) # 矩阵内行元素相加，生成数组，长度=矩阵行数
    distance = sqDistances ** 0.5 # 开方，计算欧式距离
    sortedDistIndicies = distance.argsort() # 正向排序，返回元素下标数组
    # classCount保存的K是魅力类型   V:在K个近邻中某一个类型的次数
    classCount = {} # 各类别号次数统计
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]] # 获取前k个元素的下标，对应的类别号
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1 # 对应的类别号递增1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True) # classCount中，各类别号对应的次数，倒序排序
    return sortedClassCount[0][0] # 返回次数最多的类别号

"""
文件读取处理
returnMat:特征矩阵
classLabelVector:类别号向量
"""
def file2matrix(filename):
    fr =open(filename)
    arrayOflines = fr.readlines() # readlines:是一次性将这个文本的内容全部加载到内存中(列表)
    numOfLines = len(arrayOflines) # 获取文件行数
    returnMat = np.zeros((numOfLines,3)) # 创建numOfLines*3的0矩阵，存储特征数据
    classLabelVector = [] # 存储最后一列，类别号
    index = 0
    for line in arrayOflines:
        # print("eclipse:",line) # 异常数据打印
        line = line.strip()
        # print(line.split("\t"))
        listFromline = list(map(float,line.split("\t"))) # 批量转换，并类型转换(list)，str->float
        returnMat[index,:] = listFromline[0:3] # 取前3列
        classLabelVector.append(int(listFromline[-1])) # 取最后一列
        index += 1
    return returnMat, classLabelVector


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
    normDataSet = dataSet - np.tile(minVals, (m, 1)) # 创建dataSet的对应矩阵，行列数相同，元素为dataSet每列最小值，并与dataSet相减
    normDataSet = normDataSet / np.tile(range, (m,1)) # 创建dataSet的对应矩阵，行列数相同，元素为dataSet最大最小差值，并计算，最小值/最大最小差值
    return normDataSet,range,minVals

"""
数据格式：40920飞行公里数	8.326976每周甜品克数	0.953952游戏工作时间比	3类别号
反回值：正确率
"""
def datingClassTest():
    hoRatio = 0.1
    datingDataMat, datingLabels = file2matrix("D:\\resource\\python-cluster\\data\\datingTestSet2.txt")

    # 归一化
    normMat, ranges, minVals = autoNorm(datingDataMat)

    # shape获取矩阵的行数以及列数，以二元组的形式返回的
    m = normMat.shape[0] # 取归一化矩阵行数
    numTestVecs = int(m * hoRatio) # 减少数据量，矩阵前10%的行不遍历
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],4)
        print('模型预测值: %d ,真实值 : %d' % (classifierResult,datingLabels[i]))
        if(classifierResult != datingLabels[i]):
            errorCount += 1.0  # 计算错误率
    errorRate = errorCount /float(numTestVecs)
    print("总数：%d,错误数:%d,错误率:%f" % (numTestVecs,errorCount,errorRate))
    print("正确率 : %f" % (1-errorRate))
    return 1 - errorRate


def classifyperson():
    resultList = ['没感觉', '看起来还行', '极具魅力']
    input_man = [50000, 8, 9.5]
    datingDataMat, datingLabels = file2matrix('D:\\resource\\python-cluster\\data\\datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    result = classify((input_man - minVals) / ranges, normMat, datingLabels, 10)
    print('你即将约会的人是:', resultList[result - 1])


if __name__ == '__main__':
    #     createScatterDiagram观察数据的分布情况
    # createScatterDiagram()
    acc = datingClassTest()
    if(acc > 0.9):
        classifyperson()

































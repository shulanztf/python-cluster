"""
数据可视化，积分订单数据标签化
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname="C:/Windows/Fonts/simsun.ttc", size=12)


# 定义一个将文本转化为numpy的函数
"""
returnMat:特征数据
classLabelVector:类别号向量
"""
def file2matrix(filepath):
    fr = open(filepath)  # 读取文件
    arrayLines = fr.readlines()
    numberOfLines = len(arrayLines)  # 得到行数
    returnMat = np.zeros((numberOfLines, 2))  # 构造全为0的零矩阵
    classLabelVector = []
    index = 0
    # 解析文件
    for line in arrayLines:
        # line = line.strip()  # 删除空白符（包括'\n', '\r',  '\t',  ' ')
        listFromLine = line.strip().split('\t')  # 按照('\t')进行拆分
        text = listFromLine[2:]
        print("abc:",line,text)
        returnMat[index, :] = text  # 得到特征变量
        classLabelVector.append(float(listFromLine[0]))  # 得到目标分类变量
        index += 1
    return returnMat, classLabelVector


if __name__ == '__main__':
    # 对第二列和第三列数据进行分析：
    fig = plt.figure()
    ax = fig.add_subplot(111)
    datingDataMat, datingLabels = file2matrix("D:\data\hlht\point\points-data-label\\points-label-train-20200319.txt")  # 括号是文件路径
    print(datingDataMat[:10, :])  # 数据显示
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], c=datingLabels)
    plt.xlabel("订单时间段(小时)", fontproperties=fp)
    plt.ylabel("时间窗口内订单数量", fontproperties=fp)
    ax.legend(loc='best')
    plt.show()

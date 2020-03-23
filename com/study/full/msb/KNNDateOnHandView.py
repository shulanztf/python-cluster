""""
KNN算法，数据可视化
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fp= FontProperties(fname="C:/Windows/Fonts/simsun.ttc", size=12)

#定义一个将文本转化为numpy的函数
def file2matrix(filepath):
    fr=open(filepath)#读取文件
    arraylines=fr.readlines()
    numberOfLines=len(arraylines)#得到行数
    returnMat= np.zeros((numberOfLines,3))#构造全为0的零矩阵
    classLabelVector= []
    index=0
    #解析文件
    for line in arraylines:
        line=line.strip() #删除空白符（包括'\n', '\r',  '\t',  ' ')
        listFromLine=line.split('\t') #按照('\t')进行拆分
        returnMat[index,:]=listFromLine[0:3] #得到特征变量
        classLabelVector.append(float(listFromLine[-1])) #得到目标分类变量
        index+=1
    return returnMat,classLabelVector


if __name__ == '__main__':
    #对第二列和第三列数据进行分析：
    fig=plt.figure()
    ax=fig.add_subplot(111)
    datingDataMat, datingLabels = file2matrix("D:\\resource\\python-cluster\\data\\datingTestSet2.txt")  # 括号是文件路径
    print(datingDataMat[:10,:]) # 数据显示
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2],c=datingLabels)
    plt.xlabel("花在玩电子游戏上的时间百分比",fontproperties=fp)
    plt.ylabel("每周消耗的冰淇淋升",fontproperties=fp)
    ax.legend(loc='best')
    plt.show()




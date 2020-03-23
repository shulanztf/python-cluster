
import numpy as np
import operator

# line = "312553939	2020-03-16 00:00:36"
# print(line.split("\t"))
# print(map(float, line.split("\t")))
# print(list(map(float, line.split("\t"))))
# listFromline = list(map(float, line.split("\t")))
# print(listFromline)

# dataSet = np.zeros((3,5))
# dataSet = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
dataSet = np.array([[15,16,7,18],[19,10,11,12],[34,213,21,1]])
# print(dataSet)
# print(dataSet.min(0))
# print(dataSet.max(0))
# print(dataSet.shape)
# print(dataSet.shape[0])

# print(np.tile(dataSet.min(0), (dataSet.shape[0], 1)))
# print(3 * 0.1)
# numTestVecs = int(3 * 0.1)
# print(numTestVecs)
# print(numTestVecs)
# print(dataSet[numTestVecs:3,:])
# distance = dataSet.sum(axis=1)
# print(distance ** 0.5)
# print(distance.argsort())



classCount = {}
classCount[0] =5
classCount[1] =12
classCount[2] =3
classCount[3] =9
# print(classCount)
sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True) # 各类别号次数排序
print(sortedClassCount)
print(sortedClassCount[0])
print(sortedClassCount[0][0])



























# -*- coding:utf-8 -*-
"""
@author:Subao
@file:mnist_test.py
@time:2018/6/26/10:38
"""
#首先读入mnist数据集，并把它保存在“MNIST_data”目录下
from tensorflow.examples.tutorials.mnist import input_data
#one_hot表示一个向量中只有一个值为1，其他为0
#比如[0,0,0,1,0,0,0,0,0,0],这在手写辨识中表示数字3
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
#导入tensorflow
import tensorflow as tf
#启动一个会话，tensorflow使用图来表示计算任务，在被称之为
#会话Session的上下文中执行图
sess = tf.InteractiveSession()
#初始化两个变量x,和y_，他们的维度分别是[None,784],[None,10]
#分别表示数据集图像和数据集标签
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])
#下面这两个变量W,b是我们要训练的模型参数。一会我们要运行x*W+b这个矩阵运算
#所以W和b的维度分别为[784,10],[10],并且这两个矩阵的元素全是0
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
#初始化所有变量，因为我们之前有用到tf.Variable()
sess.run(tf.initialize_all_variables())
#运行矩阵运算x*W+b，然后将这个值送入激活函数softmax(*)
y = tf.nn.softmax(tf.matmul(x, W) + b)
#计算交叉熵cross_entropy，然后把矩阵里的所有元素求和
#所以，cross_entropy是一个矢量值
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

#接下来我们开始训练模型，用梯度下降法，目标函数最小化cross_entropy
#学习率是0.01
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#训练1000次
for i in range(1000):
    #每一批的数据处理大小是50个样本
    batch = mnist.train.next_batch(50)
    #Feed的数据要用字典的形式传入，填补之前的placeholder所空着的位置
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})
#tf.argmax的作用是返回一维数组中最大的数所在的索引。
#argmax(@,1)表示按行来取最大数值索引位置，如果两个索引位置相等就返回True,否则False
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
#tf.cast()把之前correct_prediction中的布尔值，转化为“float”,
#也就是0.0或者1.0，这样一来只要对这些0和1取均值即可反映模型准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
#上述训练结束后，我们用测试集来验证模型的准确率并打印
print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
# 原文链接：https://blog.csdn.net/su_bao/article/details/80843956
"""
电影推荐系统
https://grouplens.org/datasets/movielens/ 训练数据源资源
https://www.jianshu.com/p/598ae1a31a91  需要cuda
https://blog.csdn.net/aya_tao/article/details/100056269 win10 x64 系统中tensorflow遇到ImportError: Could not find 'cudart64_100.dll'错误解决方法之一
"""
from typing import Any, Union

import pandas as pd
import numpy as np
import tensorflow as tf
from pandas import DataFrame
from pandas.io.parsers import TextFileReader

"""
数据格式: userId,movieId电影,rating评分,timestamp时间
"""
ratings_df = pd.read_csv("D:\\resource\\python-cluster\\data\\ml-latest-small\\ratings.csv")
# ratings_df.tail()
# print(ratings_df.tail(10)) # 显示数据


"""
数据格式: movieId电影,title,genres电影类别
"""
movies_df = pd.read_csv("D:\\resource\\python-cluster\\data\\ml-latest-small\\movies.csv")
# movies_df.tail(10)
# print(movies_df.tail(10))# 显示数据

movies_df["movieRow"] = movies_df.index # 为矩阵增加movieRow列
# print(movies_df.tail(10))# 显示数据

# 筛选movies_df中的特征
movies_df = movies_df[["movieRow","movieId","title"]]
movies_df.to_csv("moviesProcessed.csv",index=False,header=True,encoding="utf-8")
# print(movies_df.tail(10))# 显示数据

# 将ratings_df中的movield替换为行号
ratings_df = pd.merge(ratings_df,movies_df,on="movieId")
# print(ratings_df.head(10))# 显示数据

ratings_df = ratings_df[["userId","movieRow","rating"]]
ratings_df.to_csv("ratingsProcessed.csv",index=False,header=True,encoding="utf-8")
# print(ratings_df.head(10))# 显示数据

# 创建电影评分矩阵rating和评分记录矩阵record
userNo = ratings_df["userId"].max() + 1
movieNo = ratings_df["movieRow"].max() + 1
print(userNo)# 显示数据
print(movieNo)# 显示数据

rating = np.zeros((movieNo,userNo))
# print(rating.shape)# 显示数据,矩阵行列数

flag = 0
ratings_df_length = np.shape(ratings_df)[0]

for index,row in ratings_df.iterrows():
    rating[int(row["movieRow"]), int(row["userId"])] = row["rating"]
    flag += 1
    # print("processed %d, %d left" % (flag, ratings_df_length-flag))

record = rating > 0
# 矩阵元素类型转换，boolean->int
record = np.array(record, dtype=int)
# print(record[:2,:5])# 显示数据,矩阵前2行，前5列

# tmp1 = np.zeros((3,1))
# print(tmp1)

# 构建模型
"""
rating:电影评分表
record:评分记录表
"""
def normalizeRatings(rating,record):
    m,n = rating.shape #m电影数量,n用户数量
    rating_mean = np.zeros((m,1))
    rating_norm = np.zeros((m,n))
    for i in range(m): #遍历电影
        idx = record[i,:] !=0 #获取评过分的电影对应的用户下标向量
        rating_mean[i] = np.mean(rating[i,idx]) #计算每部电影的评分平均值
        rating_norm[i,idx] -= rating_mean[i] #用户评分-评分平均值
    return rating_norm,rating_mean # rating_norm处理后数据,rating_mean每部电影平均分

rating_norm,rating_mean = normalizeRatings(rating,record)
# print(rating_norm)
# print(rating_mean)

rating_norm = np.nan_to_num(rating_norm) #矩阵非数字元素，转成0
rating_mean = np.nan_to_num(rating_mean)
# print(rating_norm)
# print(rating_mean)


num_features = 10
# 电影内容矩阵
# X_parameters = tf.Variable(tf.random_normal_initializer([movieNo,num_features], stddev=0.35))
X_parameters = tf.Variable(tf.random.normal([movieNo,num_features], stddev=0.35))
# 用户喜好矩阵
# Theta_paramters = tf.Variable(tf.random_normal_initializer([userNo,num_features],stddev=0.35))
Theta_paramters = tf.Variable(tf.random.normal([userNo,num_features],stddev=0.35))
"""
代价表达式
X_parameters * Theta_paramters
transpose_b: 相剩前，对第二个参数Theta_paramters转置
-rating_norm,跟用户原评分相减
*record，将未评分的电影，用0代替
**2，取平方
+\ 换行
"""
# loss = 1/2 * tf.reduce_sum(((tf.matmul(X_parameters,Theta_paramters,transpose_b=True)-rating_norm)*record)**2) +\
#     1/2 * (tf.reduce_sum(X_parameters**2) + tf.reduce_sum(Theta_paramters**2))

# 创建优化器，优化目标
# optimizer = tf.train.AdamOptimizer(1e-4)
# train = optimizer.minimze(loss)

# # 四，训练模型
# tensorflow版本有差异，要调整
# tf.summary.scalar("loss", loss)
# summaryMerged = tf.summary.merge_all()
# filename = "./movie-tensorboard"
# witer = tf.summary.create_file_writer(filename)
#
# sess = tf.Session()
# init = tf.global_variables_initializer()
# sess.run(init)
#
# # 迭代训练
# for i in range(5000):
#     _,movie_summary = sess.run([train, summaryMerged])
#     witer.add_summary(movie_summary, i)

# 训练结果web界面查看,模型目录中执行命令: tensorboard --logdir=./ ,再打开 http://127.0.0.1:6006
#
# # 五，评估模型
# Current_X_parameters,Current_Theta_parameters = sess.run([X_parameters,Theta_paramtersh])
# predicts = np.dot(Current_X_parameters,Current_Theta_parameters.T) + rating_mean # .T转置
# errors = np.sqrt(np.sum((predicts-rating)**2))
# print(errors)
#
# # 六，构建完整的电影推荐系统
# user_id = input("您要向哪位用户进行推荐？请输入用户编号：")
# sortedResult = predicts[:,int(user_id)].argsort()[::-1] #倒序排序
# idx = 0
# print("为该用户推荐的评分最高的20部电影是：".center(80, "="))
# for i in sortedResult:
#     print("评分：%.2f，电影名：%s" % (predicts[i,int(user_id)]))
#     idx += 1
#     if idx == 20: break # 退出循环

print("end...")

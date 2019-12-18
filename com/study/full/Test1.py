import pandas as pd                         #导入pandas包

# https://blog.csdn.net/xz1308579340/article/details/81106310 用python读写和处理csv文件
data = pd.read_csv("/data/mysql/link_configs.csv")             #读取csv文件
print(data)                                #打印所有文件

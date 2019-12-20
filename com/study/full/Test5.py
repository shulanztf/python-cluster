# https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247484282&idx=1&sn=74af38dd9a4b169121c32cfa2ae575b9&chksm=fbdadbf7ccad52e1aa63d609c1524adcc295882ab286c8727fbca9857819460af75f0eafda65&scene=21#wechat_redirect
# 第92天：Python Matplotlib 进阶操作
import numpy as np
import matplotlib.pyplot as plt

# 绘制 x 轴数据
x = np.arange(2, 15)
y = 3 * x + 6

# 给图形设置标题
plt.title("line chart ztf")
# 设置 x 轴和 y 轴的属性名
plt.xlabel("x axis")
plt.ylabel("y axis")

# 绘制图形
plt.plot(x,y,'oc') # r颜色

# 显示图形
plt.show()

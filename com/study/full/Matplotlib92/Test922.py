"""
https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247484282&idx=1&sn=74af38dd9a4b169121c32cfa2ae575b9&chksm=fbdadbf7ccad52e1aa63d609c1524adcc295882ab286c8727fbca9857819460af75f0eafda65&scene=21#wechat_redirect
2、散点图
"""
# 导入模块
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2, 15)
y = 2 * x + 6
plt.title("scatter chart")
plt.xlabel("x axis")
plt.ylabel("y axis")

# 设置图形样式和颜色
plt.plot(x, y, "oc")
plt.show()

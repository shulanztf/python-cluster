"""
https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247484282&idx=1&sn=74af38dd9a4b169121c32cfa2ae575b9&chksm=fbdadbf7ccad52e1aa63d609c1524adcc295882ab286c8727fbca9857819460af75f0eafda65&scene=21#wechat_redirect
3、正余弦波形图
"""


import numpy as np
import matplotlib.pyplot as plt

# 计算正弦曲线上点的 x 和 y 坐标
print(np.pi)

# 绘制 x 轴，从 0 开始，
x = np.arange(0, 3 * np.pi,  0.1)
y = np.sin(x)

# 设置标题
plt.title("sine wave form")

# 绘制图形点
plt.plot(x, y, 'y')
plt.show()


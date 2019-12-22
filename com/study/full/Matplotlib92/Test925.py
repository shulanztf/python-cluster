"""
https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247484282&idx=1&sn=74af38dd9a4b169121c32cfa2ae575b9&chksm=fbdadbf7ccad52e1aa63d609c1524adcc295882ab286c8727fbca9857819460af75f0eafda65&scene=21#wechat_redirect
5、曲线图
"""

import matplotlib.pyplot as plt
import numpy as np

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.plot(X, Y - 1, color='blue', alpha=1.00)

plt.title('curve_chart1')
plt.show()

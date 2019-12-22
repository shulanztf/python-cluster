"""
https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247484282&idx=1&sn=74af38dd9a4b169121c32cfa2ae575b9&chksm=fbdadbf7ccad52e1aa63d609c1524adcc295882ab286c8727fbca9857819460af75f0eafda65&scene=21#wechat_redirect
4、直方图
"""

import matplotlib.pyplot as plt

# 设置 x 的 x 轴和 y 轴数值
x = [5, 8, 10]
y = [12, 16, 6]

# 设置 x2 的 x 轴和 y 轴数值
x2 = [6, 9, 11]
y2 = [6, 15, 7]

# 使用 bar() 函数设置条形图的颜色和对齐方式
plt.bar(x, y, color='y', align='center')
plt.bar(x2, y2, color='c', align='center')

# 设置标题
plt.title('Bar chart')
# 设置 x 轴和 y 轴的属性名
plt.ylabel('Y axis')
plt.xlabel('X axis')

# 展示图形
plt.show()

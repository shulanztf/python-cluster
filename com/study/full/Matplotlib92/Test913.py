"""
https://mp.weixin.qq.com/s?__biz=MzU1NDk2MzQyNg==&mid=2247484262&idx=1&sn=ac54fe3f9e18041c0b52da9dd34357a2&chksm=fbdadbebccad52fd25d16f183c9a36e8a8e6d3d3651f8cd5d3d8d7988a02cc7a855c4166a5b1&scene=21#wechat_redirect
3、绘图步骤
"""

import matplotlib.pyplot as plt

# 指定一个画板
fig = plt.figure()
# 指定画板后指定轴
# ax = fig.add_subplot(111)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)
ax4 = fig.add_subplot(223)
# 设置轴的位置
# ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
#        ylabel='Y-Axis', xlabel='X-Axis')
plt.show()

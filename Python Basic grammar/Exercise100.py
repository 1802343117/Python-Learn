"""
matplotlib_2:绘制折线图
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# # 准备数据
# x = np.linspace(0, 5, 10)
# y = x ** 2
#
# # 绘制折线图
# plt.plot(x, y)
# plt.title('title1')
# plt.show()
#
# # 调整线条颜色
# plt.plot(x, y, 'r')
# plt.title('title2')
# plt.show()
#
# # 修改线型
# plt.plot(x, y, 'r--')
# plt.title('title3')
# plt.show()
#
# plt.plot(x, y, 'g-*')
# plt.title('title4')
# plt.show()
#
# plt.plot(x, y, 'r-*')
# plt.title('title5')
# plt.show()
# # 添加 x, y轴label和title
# plt.plot(x, y, 'r-*')
# plt.title('title6')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
# # 添加 text 文本
# plt.plot(x, y, 'r--')
# plt.text(1.5, 10, 'y=x*x')

# 绘制爱心
x = np.linspace(-8, 8, 1024)
y1 = 0.618 * np.abs(x) - 0.5 * np.sqrt(64 - x ** 2)
y2 = 0.618 * np.abs(x) + 0.8 * np.sqrt(64 - x ** 2)
plt.plot(x, y1, color='r')
plt.plot(x, y2, color='r')
plt.show()


plt.plot(x, y1, 'r--')
plt.plot(x, y2, 'r--')
plt.show()

plt.plot(x, y1, 'b')
plt.plot(x, y2, 'b')
plt.show()

plt.plot(x, y1, 'c')
plt.plot(x, y2, 'c')
plt.show()

plt.plot(x, y1, 'Pink')
plt.plot(x, y2, 'Pink')
plt.show()
"""
输入两个正整数计算它们的最大公约数和最小公倍数
"""

x = int(input('x = '))
y = int(input('y = '))
# 如果 x 大于 y 就交换 x 和 y 的值
if x > y:
    # 通过下面的操作将 y 的值赋给 x，将 x 的值赋给 y
    x, y = y, x
# 从两个数中比较的数开始做递减的循环
for factor in range(x, 0, -1):
    if( x % factor == 0 and y % factor == 0):
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
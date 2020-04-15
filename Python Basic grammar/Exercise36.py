"""
生成式用法
生成式（推导式）可以用来生成列表，集合和字典
"""

import os

# 列表生成式生成自然数序列
list1 = list(range(1, 11))
print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 列表生成式生成自然数平方序列
list2 = [x * x for x in range(1, 11)]
print(list2)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 可以带条件
list3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list3)   # [4, 16, 36, 64, 100]

# 列出指定目标下的所有文件和目录名
list4 = [d for d in os.listdir('./res')]
print(list4)   # ['1.jpg', '1_copy.jpg', 'data.csv', 'img', 'Jack.json', 'mp3', 'test.txt', '仪表盘.html', '开到茶蘼.txt', '电商销售对比.html', '编程语言排行.html']

# 结合两个列表的不相等元素
list5 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(list5)   # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 字典生成式
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)   # {'AAPL': 191.88, 'GOOG': 1186.96, 'IBM': 149.24, 'ACN': 166.89, 'FB': 208.09}

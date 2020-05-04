"""
数据样本和清洗
"""
from random import randint, sample, shuffle, uniform

# 使用random的sample抽样10样本
lst = [randint(0, 50) for _ in range(100)]
print(lst[:5])   # [18, 46, 48, 11, 0]
lst_sample = sample(lst, 10)
print(lst_sample)   # [40, 46, 34, 37, 23, 49, 0, 28, 28, 11]

# 使用内置random中的shuffle函数冲洗数据
lst = [randint(0, 50) for _ in range(100)]
shuffle(lst)
print(lst[:5])   # [19, 33, 12, 48, 33]

# 生成满足均衡分布的坐标点
x, y = [i for i in range(100)], [round(uniform(0, 10), 2) for _ in range(100)]
print(y)

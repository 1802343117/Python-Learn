"""
基本操作
"""
# 去掉列表中的一个最小值和一个最大值，计算剩余元素的平均值
from random import randint, sample


def score_mean(lst):
    lst.sort()
    lst2 = lst[1: -1]
    return round((sum(lst2) / len(lst2)), 1)


lst = [9.1, 9.0, 8.1, 9.7, 19, 8.2, 8.6, 9.8]
result = score_mean(lst)
print('平均值：', result)  # 平均值： 9.1

# 九九乘法表
print('九九乘法表')
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d+%d=%d' % (j, i, j * i), end='\t')
    print()

# 样本抽样
print('样本抽样')
lst = [randint(0, 50) for _ in range(100)]
print(lst[:5])  # [48, 34, 18, 45, 44]
lst_sample = sample(lst, 10)
print(lst_sample)  # [28, 15, 36, 13, 13, 38, 42, 26, 34, 6]

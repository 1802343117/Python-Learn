"""
列表切片
"""

fruits = ['orange', 'apple', 'zoo', 'blueberry']
fruits += ['papaya', 'pear', 'mango']

# 列表切片
fruits2 = fruits[1:4]
print(fruits2)  # ['apple', 'zoo', 'blueberry']

# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
print(fruits3)  # ['orange', 'apple', 'zoo', 'blueberry', 'papaya', 'pear', 'mango']

fruits4 = fruits[-3:-1]
print(fruits4)  # ['papaya', 'pear']

# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)  # ['mango', 'pear', 'papaya', 'blueberry', 'zoo', 'apple', 'orange']

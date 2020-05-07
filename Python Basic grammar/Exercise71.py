"""
定义一个类
"""


class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repf__(self):
        return 'id = ' + self.id + 'name = ' + self.name


xiaoming = Student('001', 'xiaoming')
# 返回对象的哈希值
print(hash(xiaoming))  # 154902102339
# 返回对象的内存地址
print(id(xiaoming))   # 2478433637424

# 如果迭代器的所有元素都为真，返回True，否则为False
print(all([1, 0, 3, 6]))   # False
print(all([1, 2, 3]))   # True
# 如果迭代器里有一个元素为真，返回True，否则为False
print(any([0, 0, 1]))   # True

# 分别将十进制转成二进制、八进制、十六进制
print(bin(10))   # 0b1010
print(oct(9))   # 0o11
print(hex(15))   # 0xf

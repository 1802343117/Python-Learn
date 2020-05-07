"""
数学内置函数
"""

# 长度
dic = {'a': 1, 'b': 3}
print(len(dic))  # 2
a = [{'name': 'xiaoming', 'age': 18, 'gender': 'male'},
     {'name': 'xiaohong', 'age': 20, 'gender': 'female'}]
# 最大值
print(max(a, key=lambda x: x['age']))  # {'name': 'xiaohong', 'age': 20, 'gender': 'female'}
# pow(x,y,z=None,/) x为底的 y次幂，如果有z,取余
print(pow(3, 2, 4))  # 1
# 四舍五入,第二个参数代表小数点后保留几位
print(round(10.02222, 3))  # 10.022
a = [1, 4, 3, 2, 1]
# 求和
print(sum(a))  # 11
# 指定求和的初值为10
print(sum(a, 10))  # 21
# 求绝对值或复数的摸
print(abs(-6))  # 6
# 分别取商和余数
print(divmod(10, 3))  # (3, 1)
# 定义复数
print(complex(1, 2))  # (1+2j)

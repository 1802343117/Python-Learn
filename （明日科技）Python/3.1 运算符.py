'''
算数运算符的使用
'''

python = 95    # Python课程分数
english = 92   # 英语课程分数
c = 89         # C语言课程分数

sub = python - english      # 计算 Python 和 英语 的分数差
avg = (python + english + c) / 3     # 计算平均分

print("Python课程和English课程的分数差为：", sub, "分")
print("三门课程的平均成绩为：", avg, "分")
print("两种不同的除法运算符")
print("/ 结果为浮点型：", python / c)
print("// 结果为整型：", python // c)

'''
赋值运算符
'''

age = 18
age += 1    # age = age + 1
print(age)

age -= 1    # age = age - 1
print(age)

age *= 2    # age = age * 2
print(age)

age /= 2    # age = age / 2
print(age)

age //= 2   # age = age // 2
print(age)

age = 18
age //= 2   # age = age // 2
print(age)

'''
比较运算符（比较结果为：true"真" 和 false"假"）
( == )   ——>    等于
( != )   ——>    不等于
( > )    ——>    大于
( < )    ——>    小于
( >= )   ——>    大于或等于
( <= )   ——>    小于或等于
'''

python = 95    # Python课程分数
english = 92   # 英语课程分数

print("Python=", python,"English=", english)
print("python < english", python < english)
print("python > english", python > english)
print("python == english", python == english)
print("python != english", python != english)
print("python <= english", python <= english)
print("python >= english", python >= english)

'''
逻辑运算符
( and )     ——>     A and B (A、B都为 true"真" 时，返回： true"真"。否则返回：false"假")
( or )      ——>     A or B (A、B其中一个为：true"真" 时，返回： true"真"。)
'''

print("\n手机店打折活动进行中...........")
strWeek = input("请输入中文星期（如：星期一）：")                 # 输入星期
intTime = int (input("请输入时间中的小时（范围：0 ~ 23）："))     # 输入时间

if (strWeek == "星期二" and (intTime >= 10 and intTime <= 11)) or (strWeek == "星期五" and (intTime >= 14 and intTime <= 15)):
    print("恭喜您，获得了折扣参与资格！！！")
else:
    print("非常抱歉，您来晚一步，请期待下次活动.........")

'''
位运算符
位与运算符：（ & ）   ——>   有 0 即为：0
位或运算符：（ | ）   ——>   有 1 即为：1
位取反运算符：（ ~ ） ——>   0 变 1，1 变 0
位异或运算符：（ ^ ） ——>   全 0 或 全 1 才为 0
左移运算符：（ << ）  ——>   将数字左移相当于乘以 2 的 n 次幂
右移运算符：（ >> ）  ——>   将数字右移相当于除以 2 的 n 次幂
'''

# 位与运算符：（ & ）的使用，题：十进制的 12 和 8 进行位与运算
a = 12
b = 8
print(a & b)

# 位或运算符：（ | ）的使用，题：十进制的 4 和 8 进行位或运算
a = 4
b = 8
print(a | b)

# 位异或运算符：（ ^ ）的使用，题：十进制的 31 和 22 进行位异或运算
a = 31
b = 22
print(a ^ b)

# 位取反运算符：（ ~ ）的使用，题：十进制的 123 进行位取反运算
c = 123
print(~c)

# 位异或运算符：（ ^ ）的应用
pwd = input("请输入密码：")
print("原密码：", pwd)
key = input("请输入密钥")
password = int(pwd) ^ int(key)
print("加密后：", password)
print("解密后：", password ^ int(key))

# 左移运算符：（ << ）的使用
left = 2
print( left << 1)    # 左移运算符：（ << ）将数字左移相当于乘以 2 的 n 次幂

# 右移运算符：（ >> ）的使用
left = 80
print( left << 1)    # 右移运算符：（ >> ）将数字右移相当于除以 2 的 n 次幂
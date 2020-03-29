# 定义一个字符串类型的变量
python =  "学会Python还可以飞"
print(type(python))     # 输出查看该变量的类型

# 定义一个整型的变量
age = 18
print(type(age))        # 输出查看该变量的类型

# 定义一个变量 nickname
nickname = "沧海一粟"
print("这个是第一次赋值的类型：",type(nickname))   # 输出查看该变量的类型
nickname = 1024
print("这个是第二次赋值的类型：",type(nickname))   # 输出查看该变量的类型

# 定义变量 no 和 number
no = number = 2048
print("no的值为:", no,"number的值为:",number)

# 使用 Python 提供的 id函数 查看 no 和 number 的地址
print("no的地址为:", id(no),"number的地址为:", id(number))

# 通过 if 判断 no 和 number 的地址是否相同
if id(no) == id(number):
    print("no 和 number 的地址相同")
else:
    print("no 和 number 的地址不相同")
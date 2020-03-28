"""
输入100以内所有素数

说明:素数指的是只能被1和自身整除的正整数(不包括1)

"""

i = 2
print('100以内的素数：')
for num in range(2, 100):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            i = i + 1
    if i >= num:
        print(num, ' ', end = '')
print()
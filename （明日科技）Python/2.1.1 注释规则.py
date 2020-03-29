# _*_ coding: utf-8 _*_
# coding: utf-8
'''
    @ 版权所有：
    @ 文件名：2.1.1 注释规则
    @ 文件功能描述：根据身高、体重计算MBI指数
    @ 创建日期: 2019年3月29日
    @ 创建人：
    @ 修改标识：
    @ 修改描述：
    @ 修改日期：
'''

print('根据身高，体重计算BMI指数')
# 输入身高和体重
height = float(input("请输入您的身高：")) # 要求输入身高，单位为米；如：1.70
weight = float(input("请输入您的体重：")) # 要求输入体重，单位为千克；如：120

bmi = weight / (height * height) # 用于计算MBI指数，公示为："MBI = 体重 / 身高的平方"

print("您的BMI指数为：" + str(bmi))

if bmi < 18.5:
    print("您的体重过轻 `@_@` ")
if bmi >= 18.5 and bmi < 24.9:
    print("正常范围，注意保持 （-_-）")
if bmi >= 24.9 and bmi < 29.9:
    print("您的体重过重 `@_@` ")
if bmi >= 29.9:
    print("肥胖 `@_@ `")
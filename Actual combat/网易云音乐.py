"""
爬虫爬去网易云音乐
"""
# from tkinter import *
import requests

url = 'https://api.imjad.cn/cloudmusic/?type=song&id=1404885266'
resp = requests.get()
print(resp)






# # 搭建界面
#
# # 创建画板
# root = Tk()
# # 标题
# root.title('网易云音乐')
# # 设置界面大小
# root.geometry('560x450+400+200')
# # 标签控件
# label = Label(root, text='请输入下载的歌曲:', font=('华文琥珀', 20))
# # 标签定位
# label.grid()
# # 输入框
# entry = Entry(root, font=('华文琥珀', 20))
# # 定位
# entry.grid(row=0, columnspan=1)
# # 列表框
# text = Listbox(root, font=('华文琥珀', 16), width=50, heigh=15)
# # 定位 columnspan 组件横跨的列数
# text.grid(row=1, columnspan=2)
#
# # 点击按钮
# button = Button(root, text="开始下载", font=('华文琥珀', 15))
# # 定位 columnspan 组件横跨的列数
# button.grid(row=2, column=0, sticky=W)
#
# # 点击按钮
# button = Button(root, text="退出程序", font=('华文琥珀', 15))
# # 定位 columnspan 组件横跨的列数
# button.grid(row=2, column=1, sticky=E)
#
# # 显示界面
# root.mainloop()
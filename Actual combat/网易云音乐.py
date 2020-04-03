"""
爬虫爬去网易云音乐
"""

from tkinter import *
import os
from urllib.request import urlretrieve
import requests
from selenium import webdriver


def get_music():
    url = 'https://music.163.com/#/search/m/?s=%E4%B8%8B%E5%B1%B1&type=1'
    resp = requests.get(url)
    print(resp)


# 搜索歌曲

def get_music_name():
    print("开始搜索音乐")

    # 显示数据到文本框
    text.insert(END, '开始检索........')
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()

    # 获取搜索的歌名
    name = entry.get()

    # 目标地址（动态搜索）
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)

    # 目标地址（静态搜索）
    # url = 'https://music.163.com/#/search/m/?s=%E9%A3%9E%E9%A9%B0%E4%BA%8E%E4%BD%A0&type=1'

    # 指定使用 chromedriver.exe 应用（未启用隐藏浏览器功能）
    chrome_driver = "J:\Python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.get(url)

    # 隐藏浏览器
    # chrome_driver = "J:\Python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
    # option = webdriver.ChromeOptions(executable_path=chrome_driver)
    # option.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=option)
    # driver.get(url)

    driver.switch_to.frame('g_iframe')
    # 获取 歌曲id
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    print("歌曲连接", a_id)
    song_id = a_id.split('=')[-1]
    print("歌曲ID:", song_id)

    # 获取歌曲名称
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')
    print("歌曲名:", song_name)

    # 获取歌手名称
    singer_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[4]//a').get_attribute('href')
    singer_id = singer_name.split('=')[-1]
    print("歌手链接：", singer_name)
    print("歌手名:", singer_id)

    # 构造字典
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name

    # 关闭驱动
    driver.quit()

    # 下载歌曲
    # song_load(item)


# 下载歌曲
def song_load(item):
    song_id = item['song_id']
    song_name = item['song_name']

    song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)

    # 创建文件夹
    os.makedirs('music_netease', exist_ok=True)
    path = 'music_netease\{}.mp3'.format(song_name)

    # 显示数据到文本框
    text.insert(END, '歌曲：{},正在下载中.....请稍后'.format(song_name))
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()

    # 下载
    urlretrieve(song_url, path)
    print("下载歌曲成功")

    # 显示数据到文本框
    text.insert(END, '歌曲：{},以下载完毕'.format(song_name))
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()


# get_music_name()

# 搭建界面

# 创建画板
root = Tk()
# 标题
root.title('网易云音乐')
# 设置界面大小
root.geometry('620x400+400+200')
# 标签控件
label = Label(root, text='请输入下载的歌曲:', font=('微软雅黑', 20))
# 标签定位
label.grid()
# 输入框
entry = Entry(root, font=('微软雅黑', 20))
# 定位
entry.grid(row=0, column=1)
# 列表框
text = Listbox(root, font=('微软雅黑', 16), width=50, heigh=10)
# 定位 columnspan 组件横跨的列数
text.grid(row=1, columnspan=2)

# 点击按钮
button = Button(root, text="开始下载", font=('微软雅黑', 15), command=get_music_name)
# 定位 columnspan 组件横跨的列数
button.grid(row=2, column=0, sticky=W)

# 点击按钮
button = Button(root, text="退出程序", font=('微软雅黑', 15), command=root.quit)
# 定位 columnspan 组件横跨的列数
button.grid(row=2, column=1, sticky=E)

# 显示界面
root.mainloop()



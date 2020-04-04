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

    singer = ['周杰伦', '易烊千玺', '毛不易', 'Taylor Swift', '五月天', '邓紫棋', '黄家驹']

    singerId = []

    for name in singer:
        # 目标地址（动态搜索）
        # srt = "https://music.163.com/#/search/m/?s=周杰伦&type=1"
        url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)

        # 指定使用 chromedriver.exe 应用（未启用隐藏浏览器功能）
        chrome_driver = "J:\Python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_driver)
        driver.get(url)

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

        singerId.append(singer_id)

        # 关闭驱动
        driver.quit()
    print("循环迭代结束")

    print(singerId)


get_music_name()

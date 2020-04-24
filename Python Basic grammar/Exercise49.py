"""
微信好友头像图片墙
"""

import itchat
import math
import random
import os
from PIL import Image


def wechat_friend_avatar():
    # 登录微信
    itchat.login()
    # 获取好友列表
    friends = itchat.get_friends(update=True)
    for count, f in enumerate(friends):
        # 取得每位好友头像
        img = itchat.get_head_img(userName=f["UserName"])
        # 保存头像
        imgFile = open("./res/avatar/" + str(count) + ".jpg", "wb")
        imgFile.write(img)
        imgFile.close()


def picture_wall():
    x = 0
    y = 0
    # 读取目录下所有文件
    imgs = os.listdir('./res/avatar')
    # 将序列的所有元素随机排序
    random.shuffle(imgs)
    # 创建 1080 * 1080 的图片用于填充各小图片
    newImg = Image.new('RGBA', (1080, 1080))
    # 以 1080 * 1080 来拼接图片，math.sqrt() 开平方根计算每张小图片的宽高
    width = int(math.sqrt(1080 * 1080 / len(imgs)))
    # 每行图片数
    numLine = int(1080 / width)
    for i in imgs:
        img = Image.open('./res/avatar/' + i)
        # 缩小图片
        img = img.resize((width, width), Image.ANTIALIAS)
        # 拼接图片，一行排满，换行拼接
        newImg.paste(img, (x * width, y * width))
        x += 1
        if x >= numLine:
            x = 0
            y += 1
            newImg.save('./res/avatar/all.png')


if __name__ == "__main__":
    picture_wall()
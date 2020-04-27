# coding:utf-8
"""
用myqr库制作二维码
pip3 install qrcode
pip3 install myqr
"""
from MyQR import myqr
import os
from PIL import Image, ImageDraw, ImageFont


# 图片登录二维码，如使用gif背景，则可以生成动态背景效果

def img_code():
    myqr.run(words="http://dwz.date/atNM",
             # 设置容错率为最高
             version=1,
             # 控制纠错水平, 范围L, M, Q, H从左到右依次递升
             level='H',
             # 背景图
             picture='./res/1.jpg',
             # 彩色二维码
             colorized=True,
             # 用于调节图片的对比度, 1.0标识原始图片, 更小的值表示更低对比度, 更大反之, 默认为1.0
             contrast=1.0,
             # 用来调节图片的亮度，其余用法和取值同上
             brightness=1.0,
             # 保存文件的名字，格式可以是jpg,png,bmp,git
             save_name='QRCode1.png',
             # 保存位置
             save_dir=os.getcwd() + '/res/')


def draw():
    img = Image.open('./res/1.jpg')
    w, h = img.size
    txt = '另一个世界的你自己'
    draws = ImageDraw.Draw(img)
    font = ImageFont.truetype("./res/ttf/UniTortred.ttf", 26)
    draws.text((w / 2 - 100, 10), txt, (0, 0, 0), font=font)
    img.save('./res/QRCode.png')


if __name__ == '__main__':
    img_code()
    draw()

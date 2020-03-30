"""
在屏幕上显示跑马灯文字

"""

import os
import time

def main():
    content = '在人前我们总是习惯于伪装自己，但最终也蒙骗了自己'
    while True:
        # 清理屏幕上的输出
        os.system('cls') # os.system('clear')
        print("\b",content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]
if __name__ == '__main__':
    main()
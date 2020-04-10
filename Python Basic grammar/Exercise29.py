"""
写文本文件
"""


def main():
    str = '我们在等待什么奇迹，最后剩下自己舍不得挑剔'
    # w 写入,如果文件存在，则清空内容后写入，不存在则创建
    try:
        f = open("./res/test.txt", "w", encoding="utf-8")
        print(f.write(str))
        f.close()

        # a写入,文件存在,则在文件内容后追加写入,不存在则创建
        f = open("./res/test.txt", "a", encoding="utf-8")
        print(f.write(str))
        f.close()

        # with关键字系统会自动关闭文件和处理异常
        with open("./res/test.txt", "w") as f:
            f.write(str)

    except IOError as e:
        print(e)
    print('写入完毕')


if __name__ == '__main__':
    main()
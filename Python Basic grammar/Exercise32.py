from threading import Thread

import requests


# 继承Thread类创建自定义的线程类

class DownloadHandle(Thread):
    def __init__(self, url, name):
        super().__init__()
        self.url = url
        self.name = name

    def run(self):
        filename = self.name
        print(filename)
        resp = requests.get(self.url)
        with open('./res/img/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 使用了天行数据接口提供的网络API,用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get(
        'https://yz.lol.qq.com/v1/zh_cn/search/index.json')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['champions']:
        obj = mm_dict['image']
        url = obj['uri']
        name = mm_dict['name']
        # 通过多线程的方式实现图片下载
        DownloadHandle(url, name).start()


if __name__ == '__main__':
    main()

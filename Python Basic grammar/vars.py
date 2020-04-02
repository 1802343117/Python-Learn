import time

from selenium import webdriver


class WYMusic(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_cate(self, cate1, cate2):
        # 移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element_by_id("cateToggleLink"))
        # 点击 “选择分类”
        self.driver.find_element_by_id("cateToggleLink").click()
        time.sleep(1)
        # 点击华语分类
        self.driver.find_element_by_xpath(
            "//*[@id='cateListBox']/div[2]/dl[" + str(cate1) + "]/dd/a[" + str(cate2) + "]").click()
        time.sleep(1)

    def get_content_list(self):
        # 获取歌单li_list
        li_list = self.driver.find_elements_by_xpath("//*[@id='m-pl-container']/li")
        # 遍历保存title、author、click_num、url
        content_list = []
        for li in li_list:
            term = {}
            term["title"] = li.find_element_by_xpath("./p/a").text
            term["author"] = li.find_element_by_xpath("./p[2]/a").text
            term["url"] = li.find_element_by_xpath("./div/a").get_attribute("href")
            term["click_num"] = li.find_element_by_xpath("./div/div/span[2]").text
            content_list.append(term)
        # 移动到页面最底部
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # 获取下一页元素
        next_url = self.driver.find_elements_by_xpath("//a[@class='zbtn znxt']")
        return content_list, next_url

    def save_content(self, content_list):
        with open("WYMusic_all_0.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                content_str = content["title"] + "\nby " + content["author"] + "\n链接：" + content["url"] + "\n播放量：" + \
                              content["click_num"] + "\n\n"
                f.write(content_str)
        print("保存！")

    def run(self):  # 实现主要逻辑
        with open("WYMusic_all_0.txt", "w", encoding="utf-8") as f:
            f.write("")
        # 1.selenium通过控制浏览器，加载网页
        self.driver.get("https://music.163.com/#/discover/playlist/")
        # 2.使用selenium切换frame
        self.driver.switch_to.frame("g_iframe")
        # 3.获取分类
        # 获取一级分类列表
        cate1_list = self.driver.find_elements_by_xpath("//*[@id='cateListBox']/div[2]/dl")
        for i in range(1, len(cate1_list) + 1):
            cate1_name = cate1_list[i - 1].find_element_by_xpath("./dt").get_attribute("textContent")
            # 获取二级分类列表
            cate2_list = self.driver.find_elements_by_xpath("//*[@id='cateListBox']/div[2]/dl[" + str(i) + "]/dd/a")
            for j in range(1, len(cate2_list) + 1):
                cate2_name = cate2_list[j - 1].get_attribute("data-cat")
                print(cate1_name, cate2_name)
                # 3.提取数据
                while True:
                    content_list, next_url = self.get_content_list()
                    # 4.保存数据
                    self.save_content(content_list)
                    if next_url:
                        print("下一页")
                        next_url[0].click()
                        time.sleep(3)
                    else:
                        break
        print("全部下载完毕！")
        time.sleep(5)
        # 关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    music = WYMusic()
    music.run()
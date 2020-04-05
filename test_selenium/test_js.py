#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 11:02
# @Author:  haiyong
# @File:    test_js.py
import time
from selenium import webdriver

class TestJS():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("test")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()
        time.sleep(3)
        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))

    def test_datettime(self):
        self.driver.get("https://www.12306.cn/index/")
        # 使用js命令去掉readonly属性
        time_element = self.driver.execute_script(
            "dat=document.getElementById('train_date'); dat.removeAttribute('readonly')") # 注意分号后面加空格
        # 输入日期
        self.driver.execute_script("document.getElementById('train_date').value='2020-05-02'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

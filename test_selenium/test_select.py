#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/26 19:09
# @Author:  haiyong
# @File:    test_select.py
# 操作select标签
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select


class TestSelect():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_select(self):
        self.driver.get("http://sahitest.com/demo/selectTest.htm")
        ele = self.driver.find_element_by_id('s3Id')
        selected_element = Select(ele)  # 实例化Select
        # selected_text = selected_element.first_selected_option.text
        selected_element.select_by_index(1)
        print(selected_element.first_selected_option.text) # 打印当前选择的选项值
        sleep(3)
        selected_element.select_by_value("o2val")
        print(selected_element.first_selected_option.text)
        sleep(3)
        selected_element.select_by_visible_text("o3")
        print(selected_element.first_selected_option.text)
        sleep(3)



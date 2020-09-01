#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/9/1 15:34
# @Author:  haiyong
# @File:    test_locator.py
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocator():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_id(self):
        self.driver.get("https://www.baidu.com/")
        element = self.driver.find_element_by_id("kw")
        element.send_keys("test")
        # self.driver.find_element(By.ID,"kw").send_keys("test")
        assert element.get_attribute("value") == "test"


if __name__ == '__main__':
    pytest.main()











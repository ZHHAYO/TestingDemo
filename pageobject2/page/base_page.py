#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/5 16:13
# @Author:  haiyong
# @File:    base_page.py
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver


class BasePage():
    _base_url = ""
    def __init__(self, driver: WebDriver = None):
        self.driver = None
        if driver is None:
            # 1.复用已有的浏览器
            chrome_opts = webdriver.ChromeOptions()
            chrome_opts.debugger_address = "127.0.0.1:8123"
            self.driver = webdriver.Chrome(options=chrome_opts)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self._base_url != "":
            self.driver.get(self._base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

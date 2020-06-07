#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/3 12:00
# @Author:  haiyong
# @File:    test_grid.py
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

class TestGrid:
    def test_grid(self):
        # hub_url = "http://192.168.0.107:4444/wd/hub"
        # hub_url = "http://127.0.0.1:4444/wd/hub"
        # hub_url = "http://0.0.0.0:4444/wd/hub"
        hub_url = " http://localhost:4444/wd/hub"
        capability = DesiredCapabilities.CHROME.copy()
        # capability['platform'] = "WINDOWS"
        # capability['version'] = "10"
        for i in range(1,5):
            driver = Remote(command_executor=hub_url, desired_capabilities=capability)
            driver.get("https://www.baidu.com/")



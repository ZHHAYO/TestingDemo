#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/19 10:25
# @Author:  haiyong
# @File:    test_browser.py
from appium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestBrowser():
    def setup(self):
        desired_caps = {
            'platformName': 'android',
            'deviceName': '127.0.0.1:62001',
            'platformVersion': '5.1.1',
            'browserName':'Browser',
            'noReset':True,
            'automationName': 'Uiautomator2',
            'chromedriverExecutable': 'D:/testing_tools/chromedriver80/chromedriver.exe'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("test")
        search_locater = (By.ID,"index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locater))
        self.driver.find_element(*search_locater).click()
        sleep(5)

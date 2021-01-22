#!/usr/bin/python3
# -*-coding:utf-8-*-

import json
import time
from typing import List, Dict

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestCsdn:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://blog.csdn.net/u010698107")
        self.driver.implicitly_wait(10)
    def teardown_method(self):
        # self.driver.quit()
        pass

    def test_brow(self):
        # articles = self.driver.find_elements(By.XPATH, '//*[@class="article-item-box csdn-tracking-statistics"]')
        articles = self.driver.find_elements(By.XPATH, '//*[@class="article-item-box csdn-tracking-statistics"]//a')
        time.sleep(3)
        for article in articles:
            href = article.get_attribute('href')
            print(href)
            self.driver.get(href)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        # self.driver.find_element(By.XPATH, '//*[@class="article-list"]/div[1]//a').click()

        print(articles[0])
        print(len(articles))
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("test")
        # self.driver.find_element(By.ID,'kw').send_keys("test")
        # self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("test")
        # self.driver.find_element(By.CSS_SELECTOR,'id=kw').send_keys("test")
        # self.driver.find_element(By.ID, 'su').click()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # with open("cookies.txt",'w') as f:
        #     json.dump(cookies,f)
        with open("cookies.txt",'r') as f:
            # cookies = json.load(f)
            cookies:List[Dict] = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_item_title').click()# 点击添加成员

#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/18 17:38
# @Author:  haiyong
# @File:    test_browser_language.py
"""
设置浏览器语言
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# browser_locale = 'en-US'
browser_locale = 'fr-FR'
chrome_driver_path = 'D:/Python27/chromedriver.exe'

options = Options()
options.add_argument("--lang={}".format(browser_locale))

browser = webdriver.Chrome(executable_path=chrome_driver_path,
                           chrome_options=options)
browser.get('https://www.baidu.com')




















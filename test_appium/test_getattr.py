#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/18 20:01
# @Author:  haiyong
# @File:    test_getattr.py
from appium import webdriver


class TestGetAttr:
    def setup(self):
        desired_caps = {}
        # desired_caps['recreateChromeDriverSessions'] = True
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        # desired_caps['deviceName'] = 'WTKDU16813012502'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['automationName'] = 'Uiautomator2'
        # desired_caps['app'] = PATH('D:/testing_tools/tendawifi.apk')
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['newCommandTimeout'] = 3000
        # desired_caps['unicodeKeyboard'] = True
        # desired_caps['noReset'] = True
        # desired_caps['dontStopAppOnReset'] = True
        # desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeybBoard'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        # self.driver.quit()
        pass

    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))




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
        """
        打开【雪球】应用首页
        定位首页的搜索框
        判断搜索框的是否可用并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入: alibaba
        判断【阿里巴巴】是否可见
        如果可见,打印“搜索成功”点击,如果不可见,打印“搜索失败
        """
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))




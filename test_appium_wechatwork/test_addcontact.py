#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/4/23 21:25
# @Author:  haiyong
# @File:    test_addcontact.py
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAdd():
    def setup(self):
        desired_caps = {
            'platformName': 'android',
            'platformVersion': '6.0',
            'deviceName': '127.0.0.1:7555',
            'appPackage': 'com.tencent.wework',
            'appActivity': 'com.tencent.wework.launch.WwMainActivity',
            'automationName': 'Uiautomator2',
            'noReset': True,
            'unicodeKeyboard': True,
            'resetKeybBoard': True,
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_addcontact(self):
        username = "test2"
        gender = "男"
        phonenum = "12345678911"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        text = '添加成员'
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().'
                                                              'scrollable(true).instance(0)).'
                                                              f'scrollIntoView(new UiSelector().text("{text}")'
                                                              '.instance(0));').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/c56").click()
        sleep(2)
        current_act = self.driver.current_activity
        assert ".contact.controller.ContactAddActivity" in current_act
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/..//*[@resource-id='com.tencent.wework:id/ase']").send_keys(username)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/..//*[@resource-id='com.tencent.wework:id/at7']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("男")').click()
        else:
            self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("女")').click()

        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/emh").send_keys(phonenum)
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/gq7").click()
        sleep(2)
        print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']")












#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/4 18:20
# @Author:  haiyong
# @File:    test_ActionChains.py
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver. quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element_by_xpath("//*[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//*[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//*[@value='right click me']")
        action= ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_rightclick)
        action.double_click(element_doubleclick)
        sleep(3)
        action. perform()
        sleep(3)

    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_link_text("设置")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element_by_id("dragger")
        drop_element = self.driver.find_element_by_xpath("/htmL/body/div[2]")
        action= ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/htmL/body/label[1]/input")
        ele.click()
        action= ActionChains(self.driver)
        action.send_keys("testing").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("123").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


# if __name__ == '__main__':
#     pytest.main(['-v', '-s', 'test_ActionChains.py'])
#     sleep(3)



















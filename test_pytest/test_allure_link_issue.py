#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/8/23 21:07
# @Author:  haiyong
# @File:    test_allure_link_issue.py

import allure

@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass


TEST_CASE_LINK = 'https://github.com/gameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    print("这是一条测试用例的链接,链接到测试用例里面")
    pass

# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue("140","这是一个 issue")
def test_with_issue_link():
    pass
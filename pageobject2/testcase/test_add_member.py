#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/4/5 17:34
# @Author:  haiyong
# @File:    test_add_member.py
from pageobject2.page.index import Index


class TestAddMember():
    def setup(self):
        self.index = Index()

    def teardown_method(self):
        self.index.driver.quit()
    def test_add_member(self):
        add_member = self.index.goto_add_member()
        add_member.add_member()
        assert add_member.get_first() == 'test1'





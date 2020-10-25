#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/3/23 22:03
# @Author:  haiyong
# @File:    test_pytest.py
import pytest

def calc(a,b):
    return a + b


class TestDemo():
    def test_answer1(self):
        assert calc(1, 1) == 2

    def test_answer2(self):
        assert calc(2, 1) == 4

    @pytest.mark.answer3
    def test_answer3(self):
        assert calc(6, 6) == 12

if __name__=='__main__':
    pytest.main()

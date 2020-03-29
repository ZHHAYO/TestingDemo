#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/3/29 10:39
# @Author:  haiyong
# @File:    test_calc2.py
'''
pytest
'''
import pytest
import sys
sys.path.append("..")
from python.calc import Calc


class TestCalc():
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        assert self.calc.add(1, 2) == 3

    def test_add_2(self):
        assert self.calc.add(-1, -2) == -3

    def test_add_3(self):
        assert self.calc.add(1.1, 2.1) == 3.2

    def test_params(self):
        data = (1, 2)
        assert self.calc.add_1(data) == 3
        assert self.calc.add(*data) == 3

    def test_div_1(self):
        assert self.calc.div(1, 2) == 0.5

    def test_div_2(self):
        assert self.calc.div(-1, 2) == -0.5

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

data1 = [(1, 2, 3),
         (-1, -2, -3),
         (0, 1, 1),
         (0, -1, -1),
         (0.1, 0.2, 0.3),
         (999999, 1000000, 1999999)]

data2 = [(1, 2, 0.5),
          (-1, -2, 0.5),
          (0, 1, 0),
          (1, 0, 0),
          (0.1, 0.2, 0.5)]

class TestCalc():
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a, b, result", data1)
    def test_add(self, a, b, result):
        assert self.calc.add(a, b) == result



    @pytest.mark.parametrize("a, b, result", data2)
    def test_div(self, a, b, result):
        assert self.calc.div(a, b) == result


    def test_add_1(self):
        data = (1, 2)
        assert self.calc.add_1(data) == 3
        assert self.calc.add(*data) == 3

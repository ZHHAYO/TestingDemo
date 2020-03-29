#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/3/29 10:39
# @Author:  haiyong
# @File:    test_calc2.py
'''
pytest
'''
import sys
sys.path.append("..")
from python.calc import Calc
class TestCalc():
    def test_add(self):
        calc = Calc()
        assert calc.add(1,2) == 3












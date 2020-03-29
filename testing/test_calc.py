#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2020/3/29 10:12
# @Author:  haiyong
# @File:    test_calc.py
import unittest
# import sys
# sys.path.append("..")
from python.calc import Calc


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_add_1(self):
        self.assertEqual(3, self.calc.add(1, 2))

    def test_add_2(self):
        self.assertEqual(0.03, self.calc.add(0.03, 0.02))


if __name__ == '__main__':
    unittest.main()

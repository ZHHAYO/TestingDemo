#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/23 11:26
# @Author:  haiyong
# @File:    test_data.py
# 参数化

import pytest
import yaml


class TestData():
    def test_data(self):
        a=10
        b=20
        print(a+b)

    def test_data2(self):
        a = 12
        b = 20
        print(a + b)

    def test_data3(self):
        a = 13
        b = 20
        print(a + b)

    # @pytest.mark.parametrize("a,b",[(10,20),(12,20),(13,20)])
    # @pytest.mark.parametrize(("a","b"),[(10,20),(12,20),(13,20)])
    # @pytest.mark.parametrize(["a","b"],[(10,20),(12,20),(13,20)])
    @pytest.mark.parametrize(["a","b"],yaml.safe_load(open("./data.yaml")))
    def test_dataa(self,a ,b):
        print(a+b)


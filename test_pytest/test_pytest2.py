#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/3/24 21:02
# @Author:  haiyong
# @File:    test_pytest2.py
import pytest
class Test_Demo():
    def test_one(self):
        print("开始执行test_one方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行test_two方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行test_three方法")
        a = 'hello'
        b = 'hell world'
        assert a in b

if __name__=='__main__':
    # pytest.main('-v -x TestDemo')
    # pytest.main(['-v','-x','Test_Demo'])
    pytest.main()

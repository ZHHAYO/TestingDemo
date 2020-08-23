#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/3/23 22:03
# @Author:  haiyong
# @File:    test_pytest.py
import pytest
def test_one():
    print("开始执行test_one方法")
    x = 'this'
    assert 'h' in x

def test_two():
    print("开始执行test_two方法")
    x = 'hello'
    assert 'e' in x

def test_three():
    print("开始执行test_three方法")
    a = 'hello'
    b = 'hell world'
    assert a in b

if __name__=='__main__':
    pytest.main()

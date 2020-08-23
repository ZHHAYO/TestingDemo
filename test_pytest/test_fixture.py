#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/3/31 6:45
# @Author:  haiyong
# @File:    test_fixture.py
import pytest

@pytest.fixture(scope="module",params = [
    [1,1,2],
    [-1,-2,-3]
])
def data(request):
    yield request.param

class TestFixture:
    def test_add(self):
        assert 1+1==2

    def test_add2(self,data):
        assert data[0] + data[1] == data[2]

    @pytest.mark.parametrize("a,b,c",[
        [1,1,2],
        [-1,-2,-3]
    ])
    def test_add3(self,a,b,c):
        assert a + b == c

























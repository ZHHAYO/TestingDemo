#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/6/1 10:01
# @Author:  haiyong
# @File:    test_pytest.py

import random
import pytest
import yaml

data2 = [(1, 2, 0.5),
         (-1, -2, 0.5),
         (0, 1, 0),
         (1, 0, 0),
         (0.1, 0.2, 0.5)]
def data():
    with open("test_pytest_data2.yaml") as f:
        out = yaml.load(f)
        random.shuffle(out)
        print(out)
        return out

class TestParam():
    def setup(self):
        pass
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)
    def teardown(self):
        # self. driver.quit()
        pass

    # @pytest.mark.repeat(5)
    @pytest.mark.parametrize("ssid, passw", data())
    def test_yaml(self,ssid,passw):
        print("%s+%s"%(ssid,passw))
        # print(b)
        # print(result)
        assert 1 == 1

    @pytest.mark.parametrize("a, b, result", data2)
    def test_yaml2(self, a, b, result):
        result = a+b
        print("%f+%f=%f"%(a,b,result))
        # print(b)
        # print(result)
        assert a+b == result

if __name__ == '__main__':
    pytest.main(["test_pytest.py","--count=10"])


#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/9/4 16:45
# @Author:  haiyong
# @File:    test_switchTo.py
import time


def is_element_focus(self, obj, funcname, value, key, expe='pass'):
    """判断当前焦点元素是否为id

    """
    time.sleep(0.5)
    moduledict = obj.cmapdict[funcname]
    element = moduledict[key]
    prefix = element[0]
    type = element[3]
    attribute = element[4]
    # 1、切换iframe 2、获取元素 3、操作元素 4、框架切换回来
    self.switchframe(obj, prefix, flag=1)
    obj = self.getElement(obj, value, *element)
    self.switchframe(obj, prefix, flag=0)
    return obj == self.driver.switch_to.active_element
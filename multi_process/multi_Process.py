#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 16:59
# @Author:  haiyong
# @File:    multi_Process.py

from multiprocessing import Pool
from threading import Thread
# https://www.zhihu.com/question/23474039
from multiprocessing import Process

def loop():
    while True:
        pass

if __name__ == '__main__':

    for i in range(3):
        t = Process(target=loop)
        t.start()

    while True:
        pass

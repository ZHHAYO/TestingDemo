#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 15:54
# @Author:  haiyong
# @File:    calc.py
import time
import os

def long_time_task():
    print('当前进程: {}'.format(os.getpid()))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))

if __name__ == "__main__":
    print('主进程: {}'.format(os.getpid()))
    start = time.time()
    for i in range(4):
        long_time_task()

    end = time.time()
    print("用时{}秒".format((end-start)))
#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 16:33
# @Author:  haiyong
# @File:    multi_thread.py

import os
from threading import Thread

def loop(i):
    print('线程: {} - 任务{}'.format(os.getpid(), i))
    while True:
        pass

if __name__ == '__main__':

    for i in range(4):
        t = Thread(target=loop, args=(i, ))
        t.start()

    while True:
        pass




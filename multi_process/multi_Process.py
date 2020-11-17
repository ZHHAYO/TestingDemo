#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 16:59
# @Author:  haiyong
# @File:    multi_Process.py
import os
from multiprocessing import Pool
from threading import Thread
# https://www.zhihu.com/question/23474039
from multiprocessing import Process

def loop(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    while True:
        pass

if __name__ == '__main__':

    p = Pool(4)
    for i in range(4):
        p.apply_async(loop, args=(i,))

    # for i in range(3):
    #     t = Process(target=loop)
    #     t.start()

    while True:
        pass

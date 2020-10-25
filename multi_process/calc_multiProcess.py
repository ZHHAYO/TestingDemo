#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 15:58
# @Author:  haiyong
# @File:    calc_multiProcess.py

from multiprocessing import Process
import os
import time


def long_time_task(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__=='__main__':
    print('父进程: {}'.format(os.getpid()))
    start = time.time()
    p1 = Process(target=long_time_task, args=(1,))
    p2 = Process(target=long_time_task, args=(2,))
    p3 = Process(target=long_time_task, args=(3,))
    p4 = Process(target=long_time_task, args=(4,))
    print('等待所有子进程完成。')
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    end = time.time()
    print("总共用时{}秒".format((end - start)))
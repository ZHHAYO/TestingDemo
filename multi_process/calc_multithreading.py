#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/10/23 16:06
# @Author:  haiyong
# @File:    calc_multithreading.py
import os
import threading
import time


def long_time_task(i):
    print('当前子线程: {} 任务{}'.format(threading.current_thread().name, i))
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__=='__main__':
    start = time.time()
    print('主线程：{}'.format(threading.current_thread().name))
    thread_list = []
    for i in range(0, 4):
        t = threading.Thread(target=long_time_task, args=(i, ))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()

    end = time.time()
    print("总共用时{}秒".format((end - start)))
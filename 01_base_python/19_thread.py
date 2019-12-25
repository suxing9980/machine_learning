#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/20 15:06
# @Author  : Little柯南
# @File    : 19_thread.py

import _thread
import time

def print_time(threadName, delay):
    '''
    为线程定义函数
    :param threadName: 线程名字
    :param delay: 延时
    :return: None
    '''
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("{}:{}".format(threadName, time.ctime(time.time())))
    return None

if __name__ == '__main__':
    try:
        _thread.start_new_thread(print_time, ('thread-1', 2))
        _thread.start_new_thread(print_time, ('thread-2', 5))
    except:
        print('Error:无法启动线程')
    while True:
        pass
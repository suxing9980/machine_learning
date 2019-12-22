#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/20 15:16
# @Author  : Little柯南
# @File    : 20_threading.py

import threading
import time

exitFlag = 0
threadLock = threading.Lock()
class myThread(threading.Thread):


    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.m_threadID = threadID
        self.m_name = name
        self.m_counter = counter

    def run(self):
        print('开始线程：', self.m_name)
        threadLock.acquire()
        print_time(self.m_name, self.m_counter, 5)
        threadLock.release()
        print('退出线程:', self.m_name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print('{}:{}'.format(threadName, time.ctime(time.time())))
        counter -= 1

if __name__ == '__main':
    thread1 = myThread(1, 'Thread-1', 1)
    thread2 = myThread(2, 'Thread-2', 2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('退出线程……')
    while True:
        pass
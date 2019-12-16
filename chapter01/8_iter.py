#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/16 10:36
# @Author  : Little柯南
# @File    : 8_iter.py
import sys
# 类型属于对象，变量是没有类型的
list = [1,3,5,2]
it = iter(list)
#print(next(it))
#print(next(it))
#print(next(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/17 9:37
# @Author  : Little柯南
# @File    : 12_zip.py

a = [1,2,3,4,7]
b = [2,4,7,9,3]
for i, j in zip(a, b):
    print(i, ":", j)
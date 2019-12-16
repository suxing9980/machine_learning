#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/16 15:37
# @Author  : Little柯南
# @File    : 9_不定长参数.py

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def printinfo(num, *info):
    print(num)
    print(info)


def printinfo2(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return None



if __name__ == '__main__':
    printinfo(2, 2, 4, 5, 7)
    printinfo2(10)
    printinfo2(70, 60, 50)
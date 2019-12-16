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
    '''
    打印任何输入的参数
    :param arg1: 第一个参数，任何类型对象
    :param vartuple: 不定长参数
    :return: None
    '''
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return None

# 两个星号代表以字典的型式导入
# 如果单独出现星号 * 后的参数必须用关键字传入
def printnum(num, **args):
    '''
    带两个星号的参数
    :param num: number
    :param args: 不定长参数
    :return: None
    '''
    print("两个星号：")
    print(num)
    print(args)
    return None



if __name__ == '__main__':
    printinfo(2, 2, 4, 5, 7)
    printinfo2(10)
    printinfo2(70, 60, 50)
    printnum(12, a="haha", b=32)
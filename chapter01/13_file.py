#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/17 11:55
# @Author  : Little柯南
# @File    : 13_file.py

# 打开一个文件
f = open("./foo.txt", "w")

num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()
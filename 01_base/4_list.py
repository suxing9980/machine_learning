#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#@Time    : 2019/12/14 15:28
#@Author  : Little柯南
#@File    : 4_list.py

# 与Python字符串不一样的是，列表中的元素是可以改变的
# python中的函数还可以接收可变长参数，比如以 "*" 开头的的参数名，会将所有的参数收集到一个元组上
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表
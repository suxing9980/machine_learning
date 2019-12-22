#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#@Time    : 2019/12/15 22:42
#@Author  : Little柯南
#@File    : 6_dict.py

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8  # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Name']  # 删除键 'Name'
dict.clear()  # 清空字典
del dict  # 删除字典
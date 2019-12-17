#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/17 8:43
# @Author  : Little柯南
# @File    : 11_列表推导式.py

list = [2, 4, 6]
print([x*3 for x in list])
print([[x, x**2] for x in list])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
print( [3*x for x in list if x > 3])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i] for i in range(len(vec1))])
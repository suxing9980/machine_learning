#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/11/22 14:01
# @Author  : Little柯南
# @File    : rename.py

import os, os.path, time


def rename(file, keyword):
    '''
    file: 文件路径
    keyWord: 需要修改的文件中所包含的关键字
    '''
    os.chdir(file)
    items = os.listdir(file)
    print(os.getcwd())
    for name in items:
        print(name)
        # 遍历所有文件
        if not os.path.isdir(name):
            if keyword in name:
                new_name = name.replace(keyword, '')
                os.renames(name, new_name)
        else:
            # 递归
            rename(file + '\\' + name, keyword)
            os.chdir('...')
    print('-----------------------分界线------------------------')
    items = os.listdir(file)
    for name in items:
        print(name)
        return None

if __name__ == "__main__":
    rename('F:\BaiduNetdiskDownload\GO基础进阶之网络编程篇', '【瑞客论坛 www.ruike1.com】')
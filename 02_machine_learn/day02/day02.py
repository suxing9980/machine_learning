#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/11/21 14:11
# @Author  : Suxing
# @File    : day02.py

from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split
import pandas as pd

def iris():
    '''
    鸢尾花数据集
    :return: None
    '''
    ir = load_iris()
    print('获取特征值：', ir.data)
    print('获取目标值：', ir.target)
    print('获取描述：', ir.DESCR)
    print('数据集分割：')
    # 训练集特征 测试集特征 训练集标签 测试集标签 总数据集特征，总数据集标签，测试集分割系数
    x_train, x_test, y_train, y_test = train_test_split(ir.data, ir.target, test_size=0.25)
    print('训练集特征值与目标值', x_train, y_train)
    print('测试集特征值和目标值', x_test, y_test)
    return None

def news():
    '''
    20newsgroup
    :return: None
    '''
    ss = fetch_20newsgroups(data_home='./20news',subset='all')
    print(ss.data)
    print(ss.target)
    return None

def boston():
    '''
    预测波士顿房价
    :return: None
    '''
    lb = load_boston()
    print('获取特征值：', lb.data)
    print('获取目标值:', lb.target)
    print('描述:', lb.DESCR)
    return None

def knncls():
    '''
    K-近邻预测用户签到位置
    :return: None
    '''
    # 读取数据 无数据文件，找时间补起来
    # data = pd.read_csv('')
    return None

if __name__ == "__main__":
    # iris()
    boston()
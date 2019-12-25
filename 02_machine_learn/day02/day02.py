#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/11/21 14:11
# @Author  : Little柯南
# @File    : day02.py

from sklearn.datasets import load_iris, fetch_20newsgroups, load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.ensemble import RandomForestClassifier
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
    data = pd.read_csv('train.csv')
    # print(data.head(10))
    # 处理数据
    # 1、缩小数据，查询数据讯息
    data = data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")
    # 处理时间的数据
    time_value = pd.to_datetime(data['time'], unit='s')
    # print(time_value)
    # 日期格式换成字典格式
    time_value = pd.DatetimeIndex(time_value)
    # 构造一些特征
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    data = data.drop(['time'], axis=1)
    print(data)

    # 把签到数量少于n个目标位置删除
    place_count = data.groupby('place_id').count()
    tf = place_count[place_count.row_id > 3].reset_index()
    data = data[data['place_id'].isin(tf.place_id)]

    # 取出数据当中的特征值和目标值
    y = data['place_id']
    x = data.drop(['place_id'], axis=1)

    # 进行数据的分割 训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 特征工程（标准化）
    std = StandardScaler()

    # 对测试集和训练集的特征值进行标准化
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # 进行算法流程
    knn = KNeighborsClassifier()
    # fit, predict, score
    knn.fit(x_train, y_train)
    y_predict = knn.predict(x_test)
    print('预测的目标签到位置为:',y_predict)
    # 得出准确率
    print('预测的准确率:', knn.score(x_test, y_test))

    # 构造一些参数的值进行搜索
    param  = {'n_neighbors': [3,5,10]}
    gc = GridSearchCV(knn, param_grid=param, cv=2)
    gc.fit(x_train, y_train)

    # 预测准确率
    print('在测试集上准确率：',gc.score(x_test, y_test))
    print('在交叉验证中最好的结果:',gc.best_score_)
    print('选择最好的模型是:', gc.best_estimator_)
    print('每个超参数每次交叉验证的结果:', gc.cv_results_)
    return None

def naviebayes():
    '''
    朴素贝叶斯进行文本分类
    :return: None
    '''
    news = fetch_20newsgroups(subset='all')

    # 进行数据分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target,test_size=0.25)
    # 对数据集进行特征抽取
    tf = TfidfVectorizer()
    # 以训练集当中的词的列表进行每篇文章重要性统计【'a','b','c','d'】
    x_train = tf.fit_transform(x_train)
    print(tf.get_feature_names())
    x_test = tf.transform(x_test)
    # 进行贝叶斯算法的预测
    mlt = MultinomialNB(alpha=1.0)
    print(x_train)
    mlt.fit(x_train, y_train)
    y_predict = mlt.predict(x_test)
    print('预测文章的类别是:',y_predict)
    # 得出准确率
    print('准确率是:', mlt.score(x_test, y_test))
    print('每个类别的精确率和召回率:',classification_report(y_test, y_predict,target_names=news.target_names))
    return None

def decision():
    '''
    决策树对泰坦尼克号进行生死预测
    :return: None
    '''
    # 获取数据
    titan = pd.read_csv(r'http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
    # 处理数据，找出特征值和目标值
    x = titan[['pclass', 'age', 'sex']]
    y = titan['survived']

    print(x)
    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据集到训练集合测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 进行处理（特征工程） 特征---》类别---》one_hot编码
    dict = DictVectorizer(sparse=False)
    x_train = dict.fit_transform(x_train.to_dict(orient="records"))
    print(dict.get_feature_names())
    x_test = dict.transform(x_test.to_dict(orient="records"))
    print(x_train)
    # 1、用决策树进行预测
    dec = DecisionTreeClassifier()
    dec.fit(x_train, y_train)
    # 预测准确率
    print("预测的准确率:", dec.score(x_test, y_test))
    # 导出决策树的结构
    export_graphviz(dec, out_file="./tree.dot",feature_names=['年龄', "pclass=1st", 'pclass=2nd','pclass=3rd', "女性", "男性"])

    # 随机森林进行预测(超参数调优)
    # rf = RandomForestClassifier()
    # oaram = {"n_estimators":[120,200,300,500,800,1200],"max_deepth":[5,8,15,25,20]}
    # # 网络搜索与检查验证
    # gc = GridSearchCV(rf, param_grid=oaram, cv = 2)
    # gc.fit(x_train, y_train)
    # print('准确率',gc.score(x_test, y_test) )
    # print("查看选择的参数模型:", gc.best_params_)


if __name__ == "__main__":
    # iris()
    # boston()
    # knncls()
    # naviebayes()
    # decision()
    decision()
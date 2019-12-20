#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/19 17:59
# @Author  : Little柯南
# @File    : 18_socket_client.py

import socket
import sys

# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
print('host:', host)

# 设置端口号
port = 9999
# 连接服务，指定主机和端口(host, port)必须是元组,like bind
addr = (host, port)
s.connect(addr)

# 接收小于1024字节的数据
msg = s.recv(1024)
print(msg)

s.close()
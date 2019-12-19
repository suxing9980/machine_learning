#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2019/12/19 17:58
# @Author  : Little柯南
# @File    : 17_socket_server.py

import socket
import sys

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
print('hostname', host)

port = 9999

# 绑定端口号(host, port)必须是元组
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

while True:
    # 建立客户端连接
    client_socket, addr = server_socket.accept()
    print('连接地址：{}'.format(addr))
    msg = '欢迎访问菜鸟教程!' + '\r\n'
    client_socket.send(msg.encode('utf-8'))
    client_socket.close()
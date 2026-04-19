#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 11:50
# @Author  : George
# @File    : 02_use_debug.py

from flask import Flask
import json

'''
开启debug
浏览器打印异常信息
'''

app = Flask(__name__)

@app.route('/')
def helloworld():
    a = 1
    b = 0
    c = 1/0
    return c

if __name__ == '__main__':
    # host='0.0.0.0' 表示监听所有地址
    # port=8080 表示监听8080端口
    # debug=True 表示开启调试模式,当代码修改后,服务器会自动重启
    # use_reloader=False 表示不自动重启服务器
    # app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=False)
    

    # 方式二
    # app.debug = True

    # 方式三：通过修改配置参数 config
    # app.config['DEBUG'] = True

    # 方式四：通过配置文件设置 config
    app.config.from_file('config.json', json.load)
    # app.config.from_json('config.json')

    # 启动（先有配置，再启用，否则配置无效）
    app.run(host='0.0.0.0', port=8080, use_reloader=False)


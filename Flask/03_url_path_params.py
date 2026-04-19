#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 12:13
# @Author  : George
# @File    : 03_url_path_params.py

# URL 路径参数的解析使用

from flask import Flask

app = Flask(__name__)

# @app.route('/user/<int:user_id>') # /user/998
# @app.route('/user/<float:user_id>') # /user/998.5
# @app.route('/user/<string:user_id>') # /user/george
# @app.route('/user/<uuid:user_id>') # /user/6c4f163c-b9fd-44bf-880a-2e22f0030297
@app.route('/user/<int:user_id>')
def user_info(user_id):
    print(type(user_id))
    return f"获取到的用户id为：{user_id}"


# any：路径段只能是括号里列出的若干字面量之一（不是“任意类型”）
# 例：/section/about、/section/blog；/section/other 会 404
@app.route('/section/<any(about, blog, contact):name>') # /section/about
def section(name):
    return f"当前板块：{name}"


# 每个选项只占一个路径段；不能指望用 "a/b" 匹配 /x/a/b（中间斜杠会拆段）
@app.route('/doc/<any(readme, changelog, license):name>') # /doc/readme
def doc(name):
    return f"文档：{name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

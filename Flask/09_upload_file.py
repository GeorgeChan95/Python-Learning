#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/4/18 15:38
# @Author  : George
# @File    : 09_upload_file.py

'''
flask 实现文件的上传
'''

from flask import Flask, request
app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    f = request.files['pic']
    # 文件大小
    f.seek(0, 2) # 指针移动到文件末尾
    size = f.tell() # 报告当前指针位置（文件字节大小）
    print(f'文件大小：{size}')
    f.seek(0)
    print(f'name: {f.name}') # 参数名称
    print(f'filename: {f.filename}') # 文件名
    f.save(f.filename) # 保存文件
    return '上传成功'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
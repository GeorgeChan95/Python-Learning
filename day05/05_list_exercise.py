#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 13:45
# @Author  : George
# @File    : 05_list_exercise.py

# 定义一个空列表保存成绩 scores = []
scores = []
for _ in range(1, 5): # _ 是变量名，表示我们不关心循环变量的具体值，只关心循环次数
    score = float(input("请输入成绩："))
    scores.append(score)

# 输出成绩情况
print("成绩如下：", scores)
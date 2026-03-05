#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-
# @Time    : 2026/3/5 19:04
# @Author  : George
# @File    : 03_type_hint.py

# 简单类型变量标注
a:int = 10
b:float = 3.14
c:str = 'hello'
d:bool = True
e:None = None
f:bytes = b'hello'
print(a, b, c, d, e, f) # 10 3.14 hello True None b'hello'

# 复杂类型变量标注
g:list[int] = [1, 2, 3]
h:tuple[int] = (4,)
i:tuple[int, str] = (5, 'hello')
j:dict[str, int] = {'a': 1, 'b': 2}
k:set[int] = {1, 2, 3}
print(g, h, i, j, k) # [1, 2, 3] (4,) (5, 'hello') {'a': 1, 'b': 2} {1, 2, 3}


# 旧版本Python（3.10之前）
from typing import List, Tuple, Dict, Set
l:List[int] = [1, 2, 3]
m:Tuple[int] = (4,)
n:Tuple[int, str] = (5, 'hello')
o:Dict[str, int] = {'a': 1, 'b': 2}
p:Set[int] = {1, 2, 3}
print(l, m, n, o, p) # [1, 2, 3] (4,) (5, 'hello') {'a': 1, 'b': 2} {1, 2, 3}

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/2 18:37
# @Author  : George
# @File    : 001_import_module.py


# 方式一：import 模块名
# 导入math模块
import math
import random

print(math.fabs(-100))
print(random.choices([100, 200, 20 , 50]))



# 方式二: from 模块 import 方法|变量|类
from math import fabs
from random import choices
print(fabs(-2))
print(choices([1, 2, 3, 4, 5]))



# 方式三： from 模块 import 方法|变量|类 as 别名
from math import fabs as fa
from random import choices as cho
print(fa(-9))
print(cho([0, 2, 5, 76, 9]))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/2 19:20
# @Author  : George
# @File    : use_module.py

# 方式一：引入当前模块平级路径、子级路径的模块
import other_package.test_module
other_package.test_module.kk()



# 方式二：引入项目中任意路径的模块
import os
import sys

# 获取02_my_package的绝对路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"project_root: {project_root}") # project_root: E:\study\PythonLearning\Python-Learning\day07
package_path = os.path.join(project_root, '02_my_package')
other_package_path = os.path.join(project_root, 'other_package')

# 添加到sys.path
if package_path not in sys.path:
    sys.path.insert(0, package_path)

if other_package_path not in sys.path:
    sys.path.insert(0, package_path)

import jack_module
from other_package import test_module

# 使用jack_module中的函数
jack_module.hi()

test_module.kk()


# 方式3：from 包名.模块名 import *
from other_package.test_module import *
from other_package.test2 import *
kk()
cc()


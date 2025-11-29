#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/27 15:42
# @Author  : George
# @File    : 02_list_details.py


"""
列表使用注意事项和细节
"""

print("############ list定义空列表 ############")
# 1.如果我们需要一个空列表, 可以通过 [], 或者 list() 方式来定义
list1 = []
list2 = list()
print(list1, type(list1))
print(list2, type(list2))
'''
打印如下：
[] <class 'list'>
[] <class 'list'>
'''


print("############ 列表的数据项可以有多个, 而且数据类型没有限制 ############")
# 2、列表的数据项可以有多个, 而且数据类型没有限制
list3 = [1, "2", ["3", 4], True]
print(list3, type(list3))
'''
打印如下：
[1, '2', ['3', 4], True] <class 'list'>
'''


print("############ 嵌套列表 ############")
# 3、嵌套列表
list4 = [1, "2", ["3", 4], True]
print(list4, type(list4))
'''
打印如下：
[1, '2', ['3', 4], True] <class 'list'>
'''



print("############ 下标越界 ############")
# 4、列表索标必须在指定范围内使用，否则报：IndexError: list index out of range,
# 比如 list1 = [1, 2.1, 'hello'] 有效下标为 0-2
list5 = [1, 2, 3]
# print(list5[3])

'''
打印如下：
Traceback (most recent call last):
  File "E:\study\PythonLearning\Python-Learning\day05\02_list_details.py", line 50, in <module>
    print(list5[3])
          ~~~~~^^^
IndexError: list index out of range
'''


print("############ 索引也可以从尾部开始 ############")
# 5、索引也可以从尾部开始，最后一个元素的索引为 -1, 往前一位为 -2, 以此类推
list6 = ['a', 'b', 'c']
print(list6[-1]) # c
print(list6[-2]) # b
print(list6[-3]) # a
# 依然不能索引越界
# print(list6[-4])



print("############ 列表[索引]=新值 对数据进行更新, 使用 列表.append(值) 方法来添加元素 ############")
# 6、通过 列表[索引]=新值 对数据进行更新, 使用 列表.append(值) 方法来添加元素
list7 = [1, 2, 3]
print(list7[0]) # 1
list7[0] = 4
print(list7[0]) # 4
list7.append(5)
print( list7[len(list7)-1] ) # 5




print("############ 列表的元素是可以修改的, 修改后, 列表变量指向地址不变, 只是数据内容变化 ############")
# 列表的元素是可以修改的, 修改后, 列表变量指向地址不变, 只是数据内容变化
list8 = [1, 2.1, 'Hi']
print(f"list: {list8} 地址: {id(list8)} || {list8[2]} {id(list8[2])} ") # list: [1, 2.1, 'Hi'] 地址: 2370664981120 || Hi 2370665155488
list8[2] = 'python'  # 可以修改
print(f"list: {list8} 地址: {id(list8)} || {list8[2]} {id(list8[2])} ") # list: [1, 2.1, 'python'] 地址: 2370664981120 || python 2370663005232



print("############ 列表在赋值的特点：地址不变 ############")
# 扩展一下, 列表在赋值的特点,
list1 = [1, 2.1, 'Python']
list2 = list1 # list2 地址指向 list1 的地址，两个list其实就是同一个
list2[0] = 500
print("list2=", list2)  # 输出?[500, 2.1, 'Python']
print("list1=", list1)  # 输出?[500, 2.1, 'Python']



print("############ 列表在函数传参时的特点：地址不变 ############")
# 扩展一下, 看看列表在函数传参时的特点, 示意图
def f1(l):
    l[0] = 100
    print("l的id:", id(l))

list10 = [1, 2.1, 200]
print("list10的id:", id(list10))
f1(list10)
print("list10:", list10)  # 输出? [100,2.1,200]
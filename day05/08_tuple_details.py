#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/29 15:06
# @Author  : George
# @File    : 08_tuple_details.py

# tuple 的使用详情
print("########### 定义tuple空元组 ###########")
# 1.如果我们需要一个空元组, 可以通过 (), 或者 tuple() 方式来定义
tuple_a = ()
tuple_b = tuple()
print(f"tuple_a 内容是{tuple_a} 类型是{type(tuple_a)}") # tuple_a 内容是() 类型是<class 'tuple'>
print(f"tuple_b 内容是{tuple_b} 类型是{type(tuple_b)}") # tuple_b 内容是() 类型是<class 'tuple'>


# 2、元组的数据项可以有多个, 而且数据类型没有限制
print("########### tuple的数据项可以有多个, 而且数据类型没有限制 ###########")
tuple_c = (1, 'a', "Hello", 0.5, True, False)
print(tuple_c) # (1, 'a', 'Hello', 0.5, True, False)


# 3、嵌套元组
print("########### 嵌套元组 ###########")
tuple_d = (1, 2, 3, (4, 5, 6))
print(tuple_d) # (1, 2, 3, (4, 5, 6))


# 4、索引越界
print("########### 索引越界 ###########")
tuple_e = ('a', 'b', 'c')
# print("下标为3的元素：", tuple_e[3])

r"""
Traceback (most recent call last):
  File "E:\study\PythonLearning\Python-Learning\day05\08_tuple_details.py", line 31, in <module>
    print("下标为3的元素：", tuple_e[3])
                      ~~~~~~~^^^
IndexError: tuple index out of range
"""


# 5、元组的元素是不能修改
print("########### 元组的元素是不能修改 ###########")
tuple_f = ('a', 'b', 'c')
# tuple_f[1] = 'd'
r"""
Traceback (most recent call last):
  File "E:\study\PythonLearning\Python-Learning\day05\08_tuple_details.py", line 45, in <module>
    tuple_f[1] = 'd'
    ~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""


# 6、可以修改元组内 list的内容(包括 修改、增加、删除等)
print("########### 可以修改元组内 list的内容(包括 修改、增加、删除等) ###########")
tuple_f = (1, 2.1, 'Python', ["jack", "tom", "mary"])
# # 访问元组中list及其元素
print(tuple_f[3])  # ["jack", "tom", "mary"]
print(tuple_f[3][0])  # jack
# # 修改
tuple_f[3][0] = "Hi"
print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, 'Python', ["Hi", "tom", "mary"])
# tuple_f[3] = [10,20] #不能替换整个列表元素
# # 删除
del tuple_f[3][0]
print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, 'Python', ["tom", "mary"])
#
# # 增加
tuple_f[3].append("smith")
print(f"tuple_f 内容是 {tuple_f}")  # (1, 2.1, 'Python', ["tom", "mary","smith"])


# 7、索引也可以从尾部开始，最后一个元素的索引为 -1, 往前一位为 -2, 以此类推
print("########### 索引也可以从尾部开始 ###########")
tuple_g = (1, 2, 3, 4, 5)
print(tuple_g[-1]) # 5
print(tuple_g[-2]) # 4
print(tuple_g[-3]) # 3



# 8、定义只有一个元素的元组, 需要带上逗号
print("########### 定义只有一个元素的元组, 需要带上逗号 ###########")
tuple_h = (100,)
print(f"tuple_h的类型是{type(tuple_h)}") # tuple_h的类型是<class 'tuple'>

# 基本数据类型：String

import sys

name = "乔治"
age = 30
score = 90.24
gender = '男'
flag = False

print(type(name))
print(type(age))
print(type(score))
print(type(gender))
print(type(flag))
'''
<class 'str'>
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
'''

print(f"flag的类型是：{type(name)}") # flag的类型是：<class 'str'>
print(f"name的类型是：{type('George')}") # name的类型是：<class 'str'>


# Python 仅保存一份相同且不可变字符串，不同的值被存放在字符串的驻留池中，Python 的
# 驻留机制对相同的字符串只保存一份拷贝，后续创建相同字符串时，不会开辟新空间，而是把该字
# 符串的地址赋给新创建的变量。
# 字符串驻留机制
str1 = "hello"
str2 = "hello"
str3 = "hello"
# id()函数是可以返回对象/数据的内存地址
print("str1的地址：", id(str1)) # str1的地址： 2501456790368
print("str2的地址：", id(str2)) # str2的地址： 2501456790368
print("str3的地址：", id(str3)) # str3的地址： 2501456790368

str1 = "111"
print("str1的地址：", id(str1)) # str1的地址： 1836574082848
print("str2的地址：", id(str2)) # str2的地址： 2501456790368
print("str3的地址：", id(str3)) # str3的地址： 2501456790368
# 转义字符

# \t 制表符
print("George\t30");

# \n换行
print("Hi Tom\nHi Jack")

# \\ 输出\
print("D:\\software\\python")

# \" 输出"
print("乔治说：\"你好\"")

# \' 输出 '
print("乔治说：\'你好\'") # 单引号也可以不使用转义 \

# \r是回车
print("这是回车符前面的话，不会打印, \r只打印 \\r 后面的话") # \r 的作用是将光标移动到当前行的开头，但不换到下一行

# 打印内容如下：
'''
George	30
Hi Tom
Hi Jack
D:\software\python
乔治说："你好"
乔治说：'你好'
只打印 \r 后面的话
'''

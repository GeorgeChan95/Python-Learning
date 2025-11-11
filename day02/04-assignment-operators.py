# 赋值运算符的使用

a = 2
b = 3
c = 4
d = 5

a *= b
print(a) # 6


# 复合乘方赋值运算符
a = 2
a **= b
# a **= b 等价于 a = a ** b
print(a) # 8


# 复合取整除赋值运算符
a = 2
d //= a
# d //= a 等价于 d = d // a
print(d) # 2


# 复合取余赋值运算符
d = 5
d %= a
# d %= a 等价于 d = d % a
print(d) # 1


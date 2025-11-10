# 比较运算符的使用
a = 9
b = 8
print(a > b) # True
print(a >= b) # True
print(a <= b) # False
print(a < b) # False
print(a == b) # False
print(a != b) # True

flag = a > b
print("flag =", flag) # flag = True
print(a is b) # False
print(a is not b) # True



str1 = "abc#"
str2 = "abc#"
print(str1 == str2) # True
print(str1 is str2) # True, 但是在 交互模式下为False

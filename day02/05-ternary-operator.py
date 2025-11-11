# 三元运算符的使用

a = 1
b = 2
# 三元运算符的语法
    # 如果 a > b 成立，就把 a 作为整个表达式的值，并赋给变量 max。
    # 如果 a > b 不成立，就把 b 作为整个表达式的值，并赋给变量 max。
max = a if a > b else b
print(max) # 2


# 示例1
# 获取两个数的最大值
a = 10
b = 80
max = a if a > b else b
print(f"max={max}") # max=80

# 示例2
# 获取三个数的最大值
a = 10
b = 20
c = 30
max1 = a if a > b else b
print(f"max1 = {max1}") # max1 = 20

max2 = max1 if max1 > c else c
print(f"max2 = {max2}") # max2 = 30


# 示例3
# 可以支持嵌套使用，但是可读性差，不推荐
#          a              if          b          < c else c
max = (a if a < b else b) if (a if a > b else b) < c else c
print(f"max = {max}") # max = 10
# 函数作为参数

def sum(n1, n2):
    return n1 + n2

def max(n1, n2):
    return n1 if n1 > n2 else n2


def fun1(sum, max, n1, n2):
    return sum(n1, n2) + max(n1, n2)

n1 = 1
n2 = 2
print(fun1(sum, max, n1, n2))
'''
打印如下：
5
'''
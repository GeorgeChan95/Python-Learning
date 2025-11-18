# 递归函数

def test(n):
    if n > 2:
        test(n - 1)
    print(n)

test(4)
'''
# 打印结果
2
3
4
'''
print("\n------------------------------------------------ \n")

# 阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# 4! = 4 * 3! = 4 * 3 * 2! = 4 * 3 * 2 * 1! = 4 * 3 * 2 * 1 = 24
print(factorial(4))
print("\n------------------------------------------------ \n")

# fibonacci 数列
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#   f(7)  = f(6) + f(5)
#         = f(5) + f(4) + (4) + f(3)
#         = f(4) + f(3) + f(3) + f(2) + f(3) + f(2) + f(2) + f(1)
#         = f(3) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2) + f(2) + f(1) + f(2) + f(2) + f(1)
#         = f(2) + f(1) + f(2) + f(2) + f(1) + f(2) + f(1) + f(2) + f(2) + f(1) + f(2) + f(2) + f(1)
#         = 13
print(fibonacci(7))

print("\n------------------------------------------------ \n")


# 猴子吃桃问题：有一堆桃子，猴子第一天吃了其中的一半，并在多吃了一个。以后每天猴子都吃其
# 中的一半，然后再多吃一个。当到第 10 天时，想再吃时（即还没吃），发现只有 1 个桃子了。问
# 最初共多少个桃子
def peach(day):
    if(day == 10):
        return 1;
    else:
        return (peach(day + 1) + 1) * 2
total = peach(1)
print(f"最终一共有桃子{total}个")
'''
最终一共有桃子1534个
'''
print("\n------------------------------------------------ \n")


# 求函数值，已知 f(1) = 3; f(n)= 2*f(n-1)+1；请使用递归的思想，求出 f(n)的值？
def f(n):
    if(n==1):
        return 3
    else:
        return 2*f(n-1) + 1
print(f(3))
'''
打印如下：
15
'''

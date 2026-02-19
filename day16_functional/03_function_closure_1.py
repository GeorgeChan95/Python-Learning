# Python的闭包和自由变量

# 在 Python 中，如果一个变量：
# 在函数内部被使用
# 但它不是这个函数的局部变量
# 也不是全局变量
# 而是来自外层函数作用

def outer():
    x = 10

    def inner():
        # x 来自 outer，不是 inner 自己的局部变量
        return x + 1 # 这里只返回 x + 1 ， 并没有修改x 的值，因此每次x的初始值都是10

    print(f"x的值：{x}")  # x的值：10
    return inner


inn = outer()
result1 = inn()
result2 = inn()
result3 = inn()
result4 = inn()
print(f"inner执行结果：{result1}") # inner执行结果：11
print(f"inner执行结果：{result2}") # inner执行结果：11
print(f"inner执行结果：{result3}") # inner执行结果：11
print(f"inner执行结果：{result4}") # inner执行结果：11
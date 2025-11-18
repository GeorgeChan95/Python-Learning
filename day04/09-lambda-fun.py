# lambda匿名函数

def fun1(fun, num1, num2):
    print(f"fun的类型：{type(fun)}")
    return fun(num1, num2)

max_value = fun1(lambda a, b : a if a > b else b, 10, 20)
print("匿名函数返回最大值：", max_value)
'''
打印如下：
fun的类型：<class 'function'>
匿名函数返回最大值： 20
'''
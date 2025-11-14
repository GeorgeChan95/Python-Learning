# 测试调用函数返回多个结果
def f1(num1, num2):
    '''
    测试函数返回多个结果
    :param num1: 参数1
    :param num2: 参数2
    :return: 返回值有多个结果
    '''
    return num1 + num2, num2 - num1

result = f1(2, 5)
print(f"调用函数返回多个结果，结果1={result[0]}, 结果2={result[1]}")

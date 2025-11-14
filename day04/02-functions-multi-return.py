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

print("---------------------------------------------------")

def f2(param1, param2):
    return param1 + param2, param2 - param1


# 使用多个参数
r1, r2 = f2(1, 9)
print(f"r1={r1} \t r2={r2}")
# map函数：map() 是 Python 里一个非常常用的函数，用来把一个函数作用到可迭代对象的每个元素上，并返回一个新的迭代器。

def f(x):
    '''
    定义一个函数，对传入的参数做乘法操作，并返回结果
    :param x:
    :return:
    '''
    return x * 2


# 使用map函数，对集合中的每个元素，都调用 f 函数，并将结果存入 list1 中
list1 = map(f, [1, 2, 3, 4, 5])
for i in list1:
    print(i)
'''
2
4
6
8
10
'''

print("====================================")
# 使用 lamda 优化上面的代码
list2 = map(lambda x: x * 2, [1, 2, 3, 4, 5])
for i in list2:
    print(i)

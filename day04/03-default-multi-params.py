# 定义方法设置参数默认值、定义方法设置不定长参数

# 当传参为空是
def fun1(name="George", age=20):
    print(f"姓名：{name}, 年龄：{age}")

fun1("张三", 40)
# 只传参 age
fun1(age=30)
'''
打印如下：
姓名：张三, 年龄：40
姓名：George, 年龄：30
'''


# *args不是不确定是几个数，*表示[0到多]，使用可变参数/不定长参数(*args)
def fun2(*args):
    print(f"参数：{args}, 参数类型：{type(args)}")
    for num in args:
        print(f"num={num}")

fun2(1, 2, 3, 4)
'''
打印结果如下：
参数：(1, 2, 3, 4), 参数类型：<class 'tuple'>
num=1
num=2
num=3
num=4
'''


# 接收一个人的信息，但是有哪些信息是不确定的，就可以使用关键字可变参数(**kwargs)
def fun3(**kwargs):
    print(f"kwargs: {kwargs} 类型：{type(kwargs)}")
    for kwargs_name in kwargs:
        print(f"参数名：{kwargs_name} 参数值：{kwargs[kwargs_name]}")

fun3(name="george", age=18, email="george@qq.com")
# fun3(name="hsp", age=18, email="hsp@qq.com", sex="男", address="北京")
fun3()
'''
打印如下：
kwargs: {'name': 'george', 'age': 18, 'email': 'george@qq.com'} 类型：<class 'dict'>
参数名：name 参数值：george
参数名：age 参数值：18
参数名：email 参数值：george@qq.com
kwargs: {} 类型：<class 'dict'>
'''
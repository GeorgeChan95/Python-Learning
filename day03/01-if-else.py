# if-else 语句

age = int(input("请输入您的年龄："))

if age >= 18:
    print("您已经成年了")

if age > 14 and age < 18:
    print("您是个青少年")

if age <= 14:
    print("您是个儿童")
else:
    print("您是个成年人2")


if 10 > 5:
    print("10大于5")
    if 10 > 30:
        print("10大于3")
    print("这里也打印：10大于5")

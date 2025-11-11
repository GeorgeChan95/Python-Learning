# 参加Python考试，根据得分获得对应奖励
score = int(input("请输入成绩[整数]："))

if score > 0 and score <= 100:
    if score >= 90:
        print("奖励：Python证书")
    elif score >= 80:
        print("奖励：Python学习笔记")
    elif score >= 70:
        print("奖励：Python学习视频")
    else:
        print("奖励：Python学习资料")
else:
    print("输入的成绩有误")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/6 14:38
# @Author  : George
# @File    : 11_inheritance_2.py

# 如果子类和父类出现同名成员（成员属性、成员方法）， 可以通过父类名、super() 访问父类成员
# 例如：
#   父类名.成员变量
#   父类名.成员方法(self)
#   super.成员变量
#   super.成员方法()

# 1.子类不能直接访问父类的私有成员
# 2.访问不限于直接父类，而是建立从子类向上级类的查找关系 A->B->Base...

class Base:
    n3 = 800

    def fly(self):
        print("Base-fly()...")


class A(Base):
    n1 = 100
    __n2 = 600

    def run(self):
        print("A-run()....")

    def __jump(self):
        print("A-jump()....")

# B->A->Base
class B(A):

    def say(self):
        print("say()....")
        # 访问不限于直接父类，而是建立从子类向上级类的查找关系 A->B->Base...
        # Base.n3: 表示直接访问Base类的n3属性-》800
        # A.n3： 表示直接访问A类的n3 -> 800
        # super().n3: 表示从B类的直接父类A类去访问n3->800
        print(Base.n3, A.n3, super().n3) # 800 800 800
        # Base.fly(self): 表示直接访问Base的fly方法-> Base-fly()...
        # A.fly(self): 表示直接访问A类的fly方法-》Base-fly()...
        # super().fly(): 表示访问直接父类A的fly方法->Base-fly()...
        # self.fly() 表示访问本类B的fly方法->Base-fly()...
        Base.fly(self) # Base-fly()...
        A.fly(self) # Base-fly()...
        super().fly() # Base-fly()...
        self.fly() # Base-fly()...
        A.run(self) # A-run()....

b = B()
b.say()

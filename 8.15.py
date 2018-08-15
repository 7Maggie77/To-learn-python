#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 09:36:12 2018

@author: zero
"""

'''模块
' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
   
'''


'''类的实例与访问限制

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

maggie=Student('Maggie',100)
maggie.print_score()
print maggie.get_grade()
# print maggie.name    访问限制

# 不建议这么干
# maggie._Student__name='hi'
# print maggie._Student__name

# 鱼唇的行为 新增一个属性而已
# maggie.__name='hi'
# print maggie._Student__name
# print maggie.__name

'''


'''封装
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

'''


'''继承与多态
class Animal(object):
    def run(self):
        print('Animal is running...')   
    #类内，多态
    def run_twice (self):
        self.run()
        self.run()

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Timer(object):
    def run(self):
        print('Start...')

#类外，动态语言
def run_twice (animal):
    animal.run()
    animal.run()

a = Animal()
b = Dog()
c = Cat()

d = Timer()

a.run_twice()
b.run_twice()
c.run_twice()

run_twice(d)
'''


'''获取对象信息

class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=MyObject()

print hasattr(obj,'x')  # 有属性'x'吗？
print obj.x
print hasattr(obj,'y')  # 有属性'y'吗？
setattr(obj,'y',19)  # 设置一个属性'y'
print hasattr(obj,'y') 
print getattr(obj,'y')   # 获取属性'y'
print obj.y

print getattr(obj,'z',404)

print hasattr(obj,'power')
print getattr(obj,'power')
fn=getattr(obj,'power')
print fn
print fn()

'''

'''实例属性和类属性
为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加。

'''
class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1  # 这里的 Student.count 是公用的参数，具体学生 name 是单独的参数，所以是 Student,count 自加而不用涉及 self.

# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')















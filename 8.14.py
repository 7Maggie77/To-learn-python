#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:32:44 2018

@author: zero
"""

'''返回函数

###自己写的
#def createCounter():
#    def f(i):
#        def counter():
#                return i
#        return counter
#    fs=[]
#    for i in range(0,1000):
#        fs.append(f(i))
#    print(fs)
#    return fs

#将a设为容器
#def createCounter():
#    a=[0]
#    def counter():
#        a[0]=a[0]+1
#        return a[0]
#    return counter

#python3中
def createCounter():
    a=0
    def counter():
        nonlocal a  
        a=a+1
        return a
    return counter
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
    
'''

'''棋盘格（闭包 保存状态）

origin=[0,0] # 坐标系统原点
legal_x=[0,50] # x轴方向的合法坐标
legal_y=[0,50] # y轴方向的合法坐标
def create(pos=origin):
    def player(direction,step):
        # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等  
        # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。  
        new_x=pos[0]+direction[0]*step
        new_y=pos[1]+direction[1]*step
        pos[0]=new_x
        pos[1]=new_y
        # 注意！此处不能写成pos=[new_x,new_y]
        return pos
    return player

player=create() # 创建棋子player，起点为原点
print player([1,0],10) 
print player([0,1],20)
print player([-1,0],10)

'''



'''匿名函数

L=list(filter(lambda n:n%2==1,range(1,20)))
print(L)

'''

'''装饰器
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

import time,functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        fn(*args,**kw)
        stop = time.time() - start
        print('%s executed in %s ms' % (fn.__name__, stop))
        return fn(*args,**kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

'''


'''
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
------------------------------------
def decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print("begin call")
        fn(*args,**kw)
        print("end call")
        return 
    return wrapper

# 测试
@decorator
def fast(x, y):
    time.sleep(0.0012)
    print("1")
    return x + y;

@decorator
def slow(x, y, z):
    time.sleep(0.1234)
    print("2")
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)

'''
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            if callable(text):
               print('%s():' % ( func.__name__))
            else:
               print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    if callable(text):
       func=text
       return decorator(func)
    else:
       return decorator

@log('execute')
def f():
    pass

f()

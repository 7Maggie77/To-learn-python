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

#将a设为变量
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


'''匿名函数

L=list(filter(lambda n:n%2==1,range(1,20)))
print(L)

'''


'''装饰器
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：

'''

import time,functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.clock()
        fn(args, kw)
        stop = time.clock() - start
        print('%s executed in %s ms' % (fn.name, stop))
        return fn(*args, **kw)
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
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:07:05 2018

@author: zero
"""
'''filter求素数（埃氏筛法）

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
'''

'''求回数

#def integer():
#    n=1
#    while True:
#        n=n+1
#        yield n

#def pal(n):
#   if (str(n)==str(n)[::-1]):
#       return n

def is_palindrome(n):
        return str(n)==str(n)[::-1]

       
 #测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')      
'''

#排序
L = [('Alice', 75),('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
L2 = sorted(L, key=by_score)
print(L2)
        
        
        
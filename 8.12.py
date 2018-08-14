# -*- coding: utf-8 -*-
'''利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def normalize(name):
	return name.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''

from __future__ import division #在python2中得到真实小数结果
from functools import reduce
'''Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

 '''


def str2float(s):
	pos=s.find('.')
	digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':0}
	def fn(x,y):
		if y==0 :
			return x
		return x*10+y
		# for i in range(0,pos)
		# 	sum+=10**(pos-i)
		# for i in range(pos+1,length)
		# 	sum+=0.1**(i-pos)
	def char2num(s):
		return digits[s]
	return reduce(fn,map(char2num,s))/10**pos



# def str2float(s):
#     m=len(s)
#     L=list(s)
#     N=[x+1 for x in range(m) if L[x]== '.']
#     n=m-N[0]
#     def str2int(s):
#     	DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':0}
#         return DIGITS[s]
#     def int2float(x,y):
#         if y==0:
#             return x+y
#         return x*10+y
#     return reduce(int2float,map(str2int,s))/10*n


# def str2float(s):
#     def fn(x,y):
#         return x*10 + y
#     def char2num(s):
#         DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return DIGITS[s]
#     i = s.find('.')
#     right = s[:i]
#     left = s[i+1:]
#     return reduce(fn,map(char2num,right)) + reduce(fn,map(char2num,left)) / (10*i)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')





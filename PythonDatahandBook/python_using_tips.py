#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

#############列表类型的类型转换
L = list(range(10))
print(L)
print(type(L[0]))
print('\n')

L1 = [str(c) for c in L]
print(L1)
print(type(L1[0]))
print('\n')

L2 = [int(c) for c in L1]
print(L2)
print(type(L2[0]))
print('\n')

#############创建异构的列表
L3 = [True, '2', 3.0, 4]
print(L3)
print([type(item) for item in L3])


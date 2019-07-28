#! /usr/bin/env python
# -*- coding:utf-8 -*-

# numpy的线性代数库

from numpy import numpy as np

'''
函数      描述
dot 	两个数组的点积，即元素对应相乘。 相当于矩阵的乘法运算
vdot 	两个向量的点积
inner 	两个数组的内积
matmul 	两个数组的矩阵积
determinant 	数组的行列式
solve 	求解线性矩阵方程
inv 	计算矩阵的乘法逆矩阵

'''


a = np.array([[1, 2], [3, 4]])

b = np.array([[11, 12], [13, 14]])
print(a)
print('\n')
print(b)
print('\n')


print('---------dot---------')
print('[[1*11+2*13, 1*12+2*14],[3*11+4*13, 3*12+4*14]]\n')
print(np.dot(a, b))


print('---------vdot---------')
print('1*11 + 2*12 + 3*13 + 4*14 = 130\n')
print(np.vdot(a, b))


print('---------inner---------')
print('1*0+2*1+3*0')
print(np.inner(np.array([1, 2, 3]), np.array([0, 1, 0])))

print('----------matmul--------')
print('矩阵乘法')
a = [[1, 0], [0, 1]]
b = [1, 2]
print(a)
print(b)
print(np.matmul(a, b))
print(np.matmul(b, a))


print('-------numpy.linalg.det()--------')
print('-----计算输入矩阵的行列式------')

a = np.array([[1, 2], [3, 4]])

print(np.linalg.det(a))

b = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print(b)
print(np.linalg.det(b))
print(6 * (-2 * 7 - 5 * 8) - 1 * (4 * 7 - 5 * 2) + 1 * (4 * 8 - -2 * 2))

print('--------numpy.linalg.solve()--------')
print('---矩阵形式的线性方程的解----')

print('--------numpy.linalg.inv()--------')
print('---乘法逆矩阵----')


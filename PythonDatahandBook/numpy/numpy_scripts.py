#! /usr/bin/env python  
# -*- coding:utf-8 -*-  

import numpy as np
print('------------------------创建ndarray对象--------------------------')

# 列表
L1 = np.arange([1, 2, 3, 4, 5], dtype='float32')
print(L1)
print('\n')

# 嵌套列表构成多维数组
L2 = np.array([[i, i+3] for i in [2, 3, 4]])
print(L2)
print('\n')

# 使用numpy方法
L3 = np.zeros((3, 4), dtype='int')      # 全0

L4 = np.ones((3, 4), dtype='float32')   # 全1

L5 = np.full((3, 5), 3.14, dtype='float32')     # 填充

L6 = np.arange(0, 20, 2)    # 线性序列

# np.linspace()

# np.random.random()

# np.random.normal()

# np.random.randint()

# np.random.eye()

# np.random.empty()

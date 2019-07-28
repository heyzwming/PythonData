#! /usr/bin/env python
# -*- coding:utf-8 -*-

# pandas =>  高效数据结构 + 数据分析工具

# 数据类型： Series, DataFrame

# 操作： 基本操作、运算操作、特征类操作、关联类操作

#  numpy                pandas
#  基础数据类型          扩展数据类型
#  关注数据的结构表达    关注数据的应用表达
#  维度：数据间的关系    数据与索引间关系


# ------------Series---------------
# 由数据和数据索引组成
# 自动索引由0开始
# Series中的数据类型沿用numpy中的数据类型

import pandas as pd
import numpy as np


d = pd.series(range(20))


print('----------------索引----------------')
a = pd.Series([9, 8, 7, 6])

print('---------------自定义索引-----------------')
b = pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])

print('----------------创建----------------')
# python列表 标量值 Python字典 ndarray 其他函数

# 列表

l = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])

# 标量
s = pd.Series(25, index=['a', 'b', 'c'])

# 字典
d = pd.Series({'a': 7, 'b': 9, 'c': 8})
e = pd.Series({'a': 1, 'b': 2, 'c': 3}, index=['c', 'a', 'z'])

# ndarray
n = pd.Series(np.arange(5))
m = pd.Series(np.arange(5), index=np.arange(9, 4, -1))
print('----------------基本操作----------------')
# Series包括index和values，操作上类似ndarray和python的字典
# 索引方法：[]
# Numpy中运算和操作可用于Series类型
# 可以通过自定义索引的列表进行切片
# 可以通过自动索引进行切片
# 操作类似于python的字典类型(自定义索引访问 in .get )
print('---------------类型对齐操作-----------------')
# 相同索引的值进行运算，不同索引的值不进行运算
a = pd.Series([1, 2, 3], ['c', 'd', 'e'])
b = pd.Series([9, 8, 7, 6], ['a', 'b', 'c', 'd'])

print(a + b)

print('-----------------总结---------------')

# Series是一维带“标签”数组
# 基本操作类似ndarray和字典，根据索引对齐


print('--------------DataFrame------------------')

# DataFrame 类型由共用相同索引的一组列组成
# ～是一个表格型的数据类型，每列值类型可以不同
# ～既有行索引、也有列索引
# ～常用语表达二维数据，但可以表达多维数据
'''
index_0     data_a      data_1      data_w
index_1     data_b      data_2      data_x
index_2     data_c      data_3      data_x
...         ...         ...         ...
索引          多列数据

 → column   axis=1  1轴
↓
index axis=0  0轴
'''

print('-------------DataFrame类型的创建-------------------')

# 二维ndarray类型

d = pd.DataFrame(np.arange(10).reshape(2, 5))

# 以为ndarray、列表、字典、元祖或Series构成的字典

# -----字典
# 字典中的一个键值对就是DataFrame中的一列
dt = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two': pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])}

d = pd.DataFrame(dt)

e = pd.DataFrame(dt, index=['b', 'c', 'd'], columns=['two', 'three'])

# ------------------------字典实例

dl = {'城市': ['北京', '上海', '广州'],
      '环比': [101.5, 101.2, 101.3],
      '同比': [120.7, 127.3, 119.4]}
d = pd.DataFrame(dl, index=['c1', 'c2', 'c3'])


# -----列表

dl = {'one': [1, 2, 3, 4], 'two': [9, 8, 7, 6]}
d = pd.DataFrame(dl, index=['a', 'b', 'c', 'd'])

# Series类型

# 其他的DataFrame类型

print('---------------数据类型操作-----------------')

# 如何改变Series和DataFrame对象？
# 增加或重排：重新索引
# 删除：drop


# 重新索引 .reindex()
d = d.reindex(columns=['城市', '同比', '环比', '定基'])
d = d.reindex(index=['c2', 'c1', 'c0'])

# reindex 的其他参数


# 索引类型的其他方法

# .append(idx)          连接另一个Index对象，产生新Index对象
# .diff(idx)            计算差集，产生新Index对象
# .intersection(idx)    计算交集
# .union(idx)           计算并集
# .delete(loc)          删除loc位置处的元素
# .insert(loc,e)        在loc位置增加一个元素e


# .drop()能够删除Series和DataFrame指定行或列索引

# drop函数默认操作0轴元素，因为Series只有0轴，当需要使用drop函数删除1轴元素时需要指定axis = 1
# d城市信息
d.drop('c5')
d.drop('同比', axis=1)    # axis默认为0

print('--------------算术运算------------------')

# 算术运算根据行列索引，补齐(NaN)后运算，运算默认浮点数
# 维度不同时使用广播
# 二元运算会产生新的对象

a = pd.DataFrame(np.arange(12).reshape(3, 4))
b = pd.DataFrame(np.arange(20).reshape(4, 5))

print(a+b)
print(a*b)

# + - * /运算也可以使用方法：.add .sub .mul .div

# 不同维度间为广播运算，一维Series与二维DataFrame运算默认发生在轴1
b = pd.DataFrame(np.arange(20).reshape(4, 5))
c = pd.DataFrame(np.arange(4))

c-10
b-c

b.sub(c, axis=1)

# 比较运算：
# 比较运算只能比较相同索引的元素，不进行补齐
# 二维和一维、一维和零维之间为广播运算
# 采用符号进行二元运算产生布尔对象

a = pd.DataFrame(np.arange(12).reshape(3, 4))
d = pd.DataFrame(np.arange(12, 0, -1).reshape(3, 4))

a > d
a == d

# 不同维度，采用广播运算，默认在1轴

print('--------------总结------------------')

# Series  = 索引 + 一维数据
# DataFrame = 行列索引 + 二维数据

# 理解数据类型与索引的关系，操作索引即操作数据
# 重新索引、数据删除、算术运算、比较运算
# 像对待单一数据一样对待Seriesh和DataFrame对象

print('-----------------数据的排序-------------------')

# 操作索引的排序方法

# .sort_index() 在指定轴上根据索引进行排序，默认升序

b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['b', 'a', 'c', 'd'])
print(b)

b.sort_index()
b.sort_index(ascending=False)       # 降序

# 如果想要操作轴1  需要指定axis=1


# 操作数据的排序方法

# .sort_values() 指定轴上根据数值进行排序，默认升序

# Series.sort_values(axis=0,ascending=True)
# DataFrame.sort_values(by,axis=0,ascending=True)
# by: axis轴上某个索引或索引列表

c = b.sort_values(2, ascending=False)
c = c.sort_values('a', axis=1, ascending=False)

# NaN的空值同意放到末尾
print('------------------------------------')


print('------------------数据的基本统计分析------------------')



# .describe()     针对0轴的统计汇总

# Series
a = pd.Series([9, 8, 7, 6], index=['c', 'a', 'd', 'b'])
a.desribe()

a.desribe()['count']


# DataFrame
b = pd.DataFrame(np.arange(20).reshape(4,5), index=['c', 'a', 'd', 'b'])
type(b.describe())
b.describe().ix['max']  # max这一行的数据
b.describe()[2]         # 第二列的数据



print('--------------------数据的累计统计分析----------------')

# .cumsum()       依次给出前1、2、...、n个数的和
# .cumprod()                              积
# .cummax()                               最大值
# .cummin()                               最小值

# 滚动计算函数/窗口计算

# .rolling(w).sum()     依次计算相邻w个元素的和
# .rollint(w).mean()                      的算数平均值
# ............var()
#           std()
#           min()


print('----------------数据的相关分析--------------------')

# XY间的相关性： 正相关 负相关 不相关

# 方法1:协方差方法 >0 正相关
# 方法2:Pearson相关系数

print('----------------小结--------------------')

# 排序 .sort_index()          .sort_values()
# 基本统计函数 .describe()
# 累计统计函数 .cum*()        .rolling().*()
# 相关性分析 .corr()           .cov()

print('------------------------------------')
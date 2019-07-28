#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
PIL库，Python Image Library 具有强大图像处理能力的第三方库

图像->RGB值的二维向量

用numpy的二维数组表示图像


图像变换过程：
读入图像，获得RGB值，修改后保存为新的文件
"""

from PIL import Image
from numpy import numpy as np

"""
a = np.array(Image.open("image.jpg"))
print(a.shape, a.dtype)   # (457, 584, 3) uint8

print('-------RGB补值--------')
b = [255, 255, 255] - a  # 补值
im = Image.fromarray(b.astype('uint8'))
im.save("image2.jpg")

print('--------灰度图--------')
# convert：转为灰度值图片，三维数组将变为二维数组
c = np.array(Image.open('image.jpg').convert('L'))
im = Image.fromarray(c.astype('uint8'))
im.save("image3.jpg")

print('--------区间变化-------')

"""


#   图像的手绘效果

# 梯度的重构：利用像素之间的梯度值和虚拟深度值对图像进行重构
#            根据灰度的变化来模拟人类视觉的敏感程度

a = np.asarray(Image.open('image.jpg').convert('L')).astype('float')

depth = 10.  # (0-100)  预设深度值为10  取值范围0-100
grad = np.gradient(a)  # 取图像灰度的梯度值
grad_x, grad_y = grad  # 分别取x和y横纵图像梯度值
grad_x = grad_x * depth / 100.  # 根据深度调整x和y方向的梯度值
grad_y = grad_y * depth / 100.
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
vec_az = np.pi / 4.  # 光源的方位角度，弧度值
dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
dz = np.sin(vec_el)  # 光源对z 轴的影响

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8'))  # 重构图像
im.save('imageq.jpg')
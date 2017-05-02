# -*- coding:utf-8 -*-
#例7.14立方函数

def cube(side):
  side = float(side)
  cube = side*side*side
  return cube

little_box = cube(10.0)
print little_box
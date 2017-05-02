# -*- coding:utf-8 -*-
#例9.5 使用子类来计算长方体的体积

from exp9_4 import square_box

box = square_box()
print 'For a box with a square base and arbitrary height,'
print 'enter the length of the sides of its base:'
box_side = float(input())
box.set_side(box_side)
print 'Enter the height of the box: '
box_height = float(input())
box.set_height(box_height)
box.compute_volume()
print 'The volume of the box is',box.get_volume()

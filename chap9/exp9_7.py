# -*- coding:utf-8 -*-
#例9.7多态的应用

from exp9_1 import cube
from exp9_4 import square_box

box1 = cube()
box2 = square_box()
print 'Enter the length of the side of a cube:'
side1 = input()
box1.set_side(side1)
box1.compute_volume()
print 'The volume of this cube is ',box1.get_volume()
print 'For a box with a square base and arbitrary height,'
print 'enter the length of the sides of its base: '
side2 = input()
box2.set_side(side2)
print 'enter the height of the box: '
height2 = input()
box2.set_height(height2)
box2.compute_volume()
print 'The volume of this box is',box2.get_volume()

# -*- coding:utf-8 -*-
#例9.2使用类的对象

from exp9_1 import cube

print 'Enter the length of the side of a cube: '
side1 = float(input())
cube1 = cube()
cube1.set_side(side1)
cube1.compute_volume()
print 'The volume of a cube of side ',cube1.get_side()
print 'is ',cube1.get_volume()
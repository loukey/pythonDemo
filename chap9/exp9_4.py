# -*- coding:utf-8 -*-
#例9.4使用立方体类的子类,它实际上不是立方体

from exp9_1 import cube

class square_box(cube):

  def __init__(self):
    self.height = 1.0
    self.side = 1.0
    self.volume = 1.0

  def set_height(self,new_height):
    self.height = new_height

  def get_height(self):
    return self.height

  def compute_volume(self):
    self.volume = self.side**2*self.height

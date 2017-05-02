# -*- coding:utf-8 -*-
#例9.1立方体类
#__char  私有变量
#这里的文件名不使用9.1这种类型的了,因为这种类型的import读目录读取不到

class cube(object):

  def __init__(self):
    #构造函数
    self.side = 1.0
    self.volume = 1.0

  def set_side(self,new_side):
    self.side = new_side

  def compute_volume(self):
    self.volume = self.side**3

  def get_volume(self):
    return self.volume

  def get_side(self):
    return self.side
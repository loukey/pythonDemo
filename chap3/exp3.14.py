# -*- coding: utf-8 -*-
#例3.14使用case语句确定等级
#不瞒大家说,python里面并没有switch-case用法
#不过可以自己造一个～

class switch(object):
#value传入的值就是case(value)
  def __init__(self, value):
    self.value = value
    self.fall = False

#迭代器,用来在for case in swich(score)中迭代返回switch对象
  def __iter__(self):
    yield self.match
    raise StopIteration


  def match(self, *args):
    if self.fall and not args:
      return True
    elif self.value in args:
      self.fall = True
      return True
    else:
      return False

print 'Enter Score:'
score = input()
for case in switch(score):
  if case(10):
    rating = 'A'
    print rating
  if case(8 or 9):
    rating = 'B'
    print rating
  if case(6 or 7):
    rating = 'C'
    print rating
  if case(4 or 5):
    rating = 'D'
    print rating


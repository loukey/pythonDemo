# -*- coding:utf-8 -*-
#例5.11抛硬币
import math
import random

print 'Do you want to flip a coin?'
print 'Enter \'y\' for yes, \'n\' for no:'
response = raw_input()
while response == 'y':
  number = math.floor(random.uniform(0,2))#random.uniform(上限，下限)产生浮点数
  if number == 1:
    print 'Heads'
  else:
    print 'Tails'
  print 'Flip again? Enter \'y\' for yes,\'n\' for no:'
  response = raw_input()
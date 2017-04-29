# -*- coding: utf-8 -*-
#例4.32使用Floor()函数来检验用户输入
#floor()函数属于math类

import math

print 'How many wind-up mice do you want to order?'
mice_ordered = input()
while math.floor(mice_ordered) != mice_ordered:
  print 'You must enter a positive whole number.'
  mice_ordered = input()
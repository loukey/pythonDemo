# -*- coding: utf-8 -*-
#例4.28使用前置检测循环来检验数据
print 'How many wind-up mice do you want to order? -->'
mice_ordered = input()
while mice_ordered<0:
  print 'You can\'t order a negative number of mice.'
  print 'Please enter a poditive number or zero -->'
  mice_ordered = input()
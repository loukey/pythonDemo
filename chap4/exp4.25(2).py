# -*- coding: utf-8 -*-
#例4.25修改版本
print 'Enter the number of hours worked:'
print 'Enter -1 when you are done.'
hours = input()
while hours <> -1:
  print 'Enter the rate of pay:'
  rate = input()
  salary = hours * rate
  print hours,rate,salary
  print 'Enter the number of Hours worked:'
  print 'Enter -1 when you are done.'
  hours = input()
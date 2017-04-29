# -*- coding: utf-8 -*-
#例4.33使用Ceiling函数来涨工资
import math

print 'Enter number of hours worked: '
hours = input()
print 'Enter hourly pay rate: '
rate = input()
while hours<0 or rate<0:
  print 'Negative values are not allowed'
  print 'Re-enter number of hours worked:'
  hours = input()
  print 'Re-enter hourly pay rate:'
  rate = input()
pay = math.ceil(hours)*rate
print 'The pay for this employee is $',pay
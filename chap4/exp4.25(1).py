# -*- coding: utf-8 -*-
#例一个计算薪水的哨兵控制器循环
print 'Enter the number of hours this employee worked:'
print 'Enter -1 when you are done.'
hours = input()
while hours != -1:
  print 'Enter this employee\'s rate of pay:'
  rate = input()
  salary = hours * rate
  print 'An employee who worked',hours
  print 'receives a salary of $',salary
  print 'Enter the number of hours this emplyee worked:'
  print 'Enter -1 when your are done.'
  hours = input()
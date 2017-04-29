# -*- coding:utf-8 -*-
#例5.6统计用户输入

positive_count = 0
negative_count = 0
print 'Enter a number. Enter 0 When done:'
number = input()
while number!=0:
  if number>0:
    positive_count += 1
  else:
    negative_count += 1
  print 'Enter a number. Enter 0 when done:'
  number = input()
print 'The number of positive numbers entered is ',positive_count
print 'The number of negative numbers entered is ',negative_count
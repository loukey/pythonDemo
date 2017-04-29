# -*- coding: utf-8 -*-
#例4.7使用计数器显示数字平方

print 'Please enter a positive integer:'
positive_integer = input()
count = 1
while count<=positive_integer:
  print count," ",count*count
  count += 1
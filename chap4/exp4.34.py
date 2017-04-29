# -*- coding: utf-8 -*-
#例应用循环进行求和
sum = 0
print 'Enter a positive number. Enter 0 when done:'
number = input()
while number>0:
  sum += number
  print 'Enter a positivve number. Enter 0 When done:'
  number = input()
print 'The sum of the numbers input is',sum
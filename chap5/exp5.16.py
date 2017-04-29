# -*- coding:utf-8 -*-
#例5.16使用Repeat...until和while循环嵌套

while True:
  sum = 0
  print 'I can do addition for you!'
  print 'Enter the first number you want to add:'
  print 'Enter 0 when you\'re done.'
  number = input()
  while number!=0:
    sum += number
    print 'Enter your next number or 0 if you are done:'
    number = input()
  print 'The sum of your numbers is ',sum
  print 'Sum another list of numbers?(Y or N)'
  response = raw_input()
  if response == 'N':
    break
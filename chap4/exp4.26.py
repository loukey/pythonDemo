# -*- coding: utf-8 -*-
#例4.26要知道什么时候停止,提问就行

while True:
  print 'Enter the number of hours worked.'
  hours = input()
  print 'Enter the rate of pay:'
  rate = input()
  salary = hours * rate
  print 'An employee who worked',hours
  print 'at the rate of ',rate,'per hour'
  print 'receives a salary of $',salary
  print 'Process another employee? (Y or N)'
  response = raw_input()
  if response == 'N':
    break
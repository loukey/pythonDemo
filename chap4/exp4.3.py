# -*- coding: utf-8 -*-
#例4.3危险的无限循环
#这是个无限循环..大家手动停了一下

while True:
  print 'Please enter a number:'
  number = input()
  computer_number = number + 1
  print number
  if number>computer_number:
    break
print 'The End'
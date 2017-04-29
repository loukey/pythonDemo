# -*- coding:utf-8 -*-
#例5.5使用While循环计算有效的平方根
import math

print 'Do you want to find the square root of a number?'
print 'Enter \'y\' for yes,\'n\' for no: '
response = raw_input()
while response == 'y':
  print 'Enter a positive number:'
  number = input()
  if number>=0:
    root = math.sqrt(number)
    print 'The square root of ',number,'is: ',root
  else:
    print 'Your number is invalid.'
  print 'Do you want to do this again?'
  print 'Enter \'y\' for yes,\'n\' for no: '
  response = raw_input()

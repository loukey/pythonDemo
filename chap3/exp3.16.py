# -*- coding: utf-8 -*-
#例3.16输出数字的倒数

print 'Enter a number.'
print 'This program will display its reciprocal.'
number = input()
if number != 0:
  reciprocal = 1/float(number)
  print 'The reciprocal of',number,'is',reciprocal
else:
  print 'The reciprocal if 0 is not defined'
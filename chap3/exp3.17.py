# -*- coding: utf-8 -*-
#例3.17避免Sqrt()函数的非法操作
#sqrt()函数来自于math库,需要先引用
import math

print 'Enter a number.'
print 'This program will display its square root.'
number = input()
if number >= 0:
  print 'The square root of',number,'is',math.sqrt(number),'.'
else:
  print 'square root of',number,'is not defined'
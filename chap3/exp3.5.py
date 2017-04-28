# -*- coding: utf-8 -*-
#例3.5用OR运算符节省时间和空间

# number = input('输入一个数字')
# if number<5:
#   print 'OK'
# if number>10:
#   print 'OK'

#上面注释的代码用OR优化
number = input()
if number<5 or number>10:
  print 'OK'
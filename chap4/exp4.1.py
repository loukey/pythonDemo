# -*- coding: utf-8 -*-
#例4.1简单地打印数字
#很有趣的是,Python没有do..while以及while..until
#但是我们也可以强行实现

while True:
  print 'Please enter a number:'
  number = input()
  print number
  if number==0:
    break
print 'List Ended'

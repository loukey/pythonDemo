# -*- coding: utf-8 -*-
#例4.8用递减计数器进行发射倒计数

count = 100
print 'Countdown in...'
while count>0:
  print count,' seconds'
  count += -1
print 'Blastoff!'
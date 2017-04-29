# -*- coding:utf-8 -*-
#例5.19训练2:中级
y = 3
count1 = 1
while True:
  x = count1 + 1
  count2 = 1
  print 'Pass NUmber ',count1
  while count2<=y:
    z = y*x
    print 'X= ',x,', Y=',y,', Z=',z
    x += 1
    count2 += 1
  count1 += 1
  if not count1<y:
    break
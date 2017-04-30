# -*- coding:utf-8 -*-
#例6.5数组让编程变得容易且简洁

names = []
count = 0
print 'Enter a name.(Enter * to quit.)'
temp_name = raw_input()
while temp_name != '*':
  names.append(temp_name)
  count += 1
  print 'Enter a name.(Enter * to quit.)'
  temp_name = raw_input()
k = count-1
while k>=0:
  print names[k]
  k += -1

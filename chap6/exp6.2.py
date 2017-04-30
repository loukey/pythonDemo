# -*- coding:utf-8 -*-
#例6.2用数组计算降雨量

sum = 0
rain = []
for k in range(0,12):
  print 'Enter rainfall for month',k+1
  rain.insert(k,float(input()))
  sum += rain[k]
average = sum/12
for k in range(0,12):
  print 'Rainfall for Month ',k+1,'is',rain[k]
print 'The average monthly rainfall is',average
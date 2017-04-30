# -*- coding:utf-8 -*-
#例6.3你将热衷于平行数组

max = 0
k = 0
names = ['']
sales = [0.0]
print 'Enter a salesperson\'s name and monthly sales. '
print 'Enter *, 0 when done.'
while names[k] != '*':
  if sales[k] > max:
    index = k
    max = sales[index]
  k += 1
  print 'Enter name and sales(enter*,0 when done).'
  names.insert(k,raw_input())
  sales.insert(k,float(input()))
print 'Maximum sales for the month: ',max
print 'Salesperson: ',names[index]
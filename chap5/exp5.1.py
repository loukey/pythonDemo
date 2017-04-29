# -*- coding:utf-8 -*-
#例5.1当钱花完的时候，退出循环
total = 0
print 'Enter the maximum amoount you want to spend: $'
max = input()
for count in range(1,11):
  print 'Enter the cost of an item: '
  cost = input()
  total += cost
  if total>max:
    print 'You have reached your spending limit.'
    print 'You cannot buy this item or anything else.'
    total += -cost
    break
  print 'You have bought ',count,' items .'
print 'Your total cost is $ ',total

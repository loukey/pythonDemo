# -*- coding:utf-8 -*-
#例6.13对含有大量元素的数组进行排序
import random

#用random随机生成一个200的数组
args = [random.uniform(1,100) for i in range(200)]
n = 199
m = 0
temp = 0
k = 0
while k<n:
  youngest = args[k]
  index = k
  j = k+1
  while j<=n:
    if args[j] < youngest:
      youngest = args[j]
      index = j
    j += 1
  if k!= index:
    temp = args[k]
    args[k] = args[index]
    args[index] = temp
  k += 1
print 'ages sorted: '
while m<n+1:
  print args[m]
  m += 1

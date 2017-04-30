# -*- coding:utf-8 -*-
#例6.10找到正确的'House'
#好....好像没有任何输出?!

n = 10
# key = 'House'
key = 3
low = 0
high = n
found = 0
index = int(n/2)
# words = ['Aardvark','Book','Dog','House','Job','Month','Start','Top','Total','Work','Zebra']
words = [0,1,2,3,4,5,6,7,8,9,10]
while found==0 and low<=high:
  if key < words[index]:
    high = index-1
    index = int(high+low)/2
  else:
    if key>words[index]:
      low = index+1
      index = int(high+low)/2
    else:
      found = 1
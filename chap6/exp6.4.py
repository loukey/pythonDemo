# -*- coding:utf-8 -*-
#例6.4使用数组的好处

sum = 0
count1 = 0
medieval = []
print 'Enter a test score(or 999 to quit):'
score = float(input())
while score != 999:
  medieval.insert(count1,score)
  count1 += 1
  sum += score
  print 'Enter another score or 999 to quit:'
  score = float(input())
average = sum/count1
count2 = 0
k = 0
while k<count1:
  if medieval[k]>average:
    count2 += 1
  k += 1
print 'The average is:',average
print 'The number of scores above the average is :',count2
print 'The number of scores below the average is :',count1-count2
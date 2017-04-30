# -*- coding:utf-8 -*-
#例6.20一应俱全的友好版本
import numpy as np

#这里注意要把30个名字自己初始化了!!
names = ['jack']*30
scores = np.ndarray(shape=(30,5))
count = 0
print 'Enter a student\'s name; enter * when done.'
student_name = raw_input()
while student_name != '*':
  names[count] = student_name
  print 'Enter 5 test scores for ',names[count]
  test = 0
  while test<5:
    scores[count][test] = float(input())
    test += 1
  count += 1
  print 'Enter a student\'s name; enter * when done.'
  student_name = raw_input()
k = 0
while k<= count-1:
  sum = 0
  j = 0
  while j<5:
    sum += scores[k][j]
    j += 1
  average = sum/5
  print names[k],': ',average
  k += 1
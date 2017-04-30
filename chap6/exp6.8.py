# -*- coding:utf-8 -*-
#例6.8输入数字,排序输出

test_scores = []
print 'Enter a test score; enter -9999 when done:'
one_score = float(input())
count = 0
while one_score != -9999:
  test_scores.append(one_score)
  count += 1
  print 'Enter a test score; enter -9999 when done:'
  one_score = float(input())
flag = 0
while flag==0:
  flag = 1
  k = 0
  while k<= count-2:
    if test_scores[k]<test_scores[k+1]:
      temp = test_scores[k]
      test_scores[k] = test_scores[k+1]
      test_scores[k+1] = temp
      flag = 0
    k += 1
print 'Sorted list...'
k = 0
while k<= count-1:
  print test_scores[k]
  k += 1
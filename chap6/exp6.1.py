# -*- coding:utf-8 -*-
#例6.1给数组元素赋值

scores = []
#要输25个也太多了。。。大家测试可以改小一点
for k in range(0,25):
  print 'Enter score: '
  scores.insert(k,input())

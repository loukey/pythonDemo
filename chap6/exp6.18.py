# -*- coding:utf-8 -*-
#例6.18使用嵌套For循环输入二维数组
import numpy as np

scores = np.ndarray(shape=(30,5))
for student in range(0,30):
  print 'Enter 5 test scores for student',student+1
  for test in range(0,5):
    scores[student][test] = input()


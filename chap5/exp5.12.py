# -*- coding:utf-8 -*-
#例5.12掷骰子
import math
import random

five_count = 0
eight_count = 0
for K in range(1,1001):
  die1 = math.floor(random.uniform(0,6))+1
  die2 = math.floor(random.uniform(0,6))+1
  sum = die1 + die2
  if sum==5:
    five_count += 1
  if sum==8:
    eight_count += 1
print 'Number of times sum was 5:',five_count
print 'Number of times sum was 8:',eight_count

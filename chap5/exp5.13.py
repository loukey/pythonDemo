# -*- coding:utf-8 -*-
#例5.13新的猜数字游戏
import math
import random

given = math.floor(random.uniform(0,100))+1
print 'I\'m thinking of a whole number from 1 to 100. '
print 'Can you guess what it is?'
while True:
  print 'Enter your guess:'
  guess = input()
  if guess<given:
    print 'You\'re too low.'
  if guess>given:
    print 'You\'re too high.'
  if guess==given:
    break
print 'Congratulations! You win!'
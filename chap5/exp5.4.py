# -*- coding:utf-8 -*-
#例5.4重写猜数字游戏
import os

print 'Enter a secret number:'
secret_number = input()
os.system('clear')
count = 1
while True:
  guess = input()
  if guess == secret_number:
    print 'You guessed it!'
    break
  else:
    print 'Try again'
  count += 1
  if count>5 :
    break
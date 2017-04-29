# -*- coding:utf-8 -*-
#例5.3简单的猜数字游戏
import os

print 'Enter a secret Number:'
secret_number = input()
os.system('clear')#linux,mac下用这个, windows下用os.system('cls'),IDE中不起作用
for count in range(1,6):
  print 'Guess the secret number:'
  guess = input()
  if guess == secret_number:
    print 'You guessed it!'
    break
  else:
    print 'Try again'
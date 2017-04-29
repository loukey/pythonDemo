# -*- coding:utf-8 -*-
#例5.2只对整数求和

sum = 0
for count in range(1,11):
  print 'Enter an integer:'
  number = input()
  if number != int(number):
    print 'Your entry is not an integer.'
    print 'The summation has ended.'
  else:
    sum += number
print 'The sum of your numbers is :',sum
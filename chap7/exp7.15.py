# -*- coding:utf-8 -*-
#例7.15使用函数找出最省油的路段
#测试输入的count<10和k<10比较大,大家可以减小一点!

def answer(num1,num2):
  return float(num1)/float(num2)

trip_name = [" "]*10
trip_miles = [0.0]*10
trip_mpg = [0.0]*10
count = 0
while count<10:
  print 'Enter a description of this trip: '
  name = raw_input()
  trip_name[count] = name
  print 'How many miles did you drive? '
  miles = float(input())
  trip_miles[count] = miles
  print 'How mant gallons of gas did you use on this trip? '
  gallons = float(input())
  trip_mpg[count] = answer(miles,gallons)
  count += 1
k = 0
print 'Trip Name \t Miles Traveled \t MPG'
while k<10:
  print trip_name[k],'\t',trip_miles[k],'\t',trip_mpg[k]
  k += 1


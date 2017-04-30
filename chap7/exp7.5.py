# -*- coding:utf-8 -*-
#例7.5在哪里改变变量的值

def change_value(*number):
  number = 2
  return number

number_one = 1
number_one = change_value(number_one)
print number_one
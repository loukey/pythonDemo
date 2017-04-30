# -*- coding:utf-8 -*-
#例7.6引用传递和值传递
#python传值的参数类型:数字,字符串,元组
#传址:list,dictionary
#总而言之,如果是可变的,就是传址

def switch(number1,number2):
  number1 = 293
  number2 = 156
  return number1,number2

my_number = 156
your_number = 293
my_number,your_number = switch(my_number,your_number)
# -*- coding:utf-8 -*-
#例5.9使用Length_Of()函数进行格式化输出
count = 0
print 'Enter your name: '
name = raw_input()
print 'Choose one of the following symbols: '
print ' * or #'
symbol = raw_input()
print 'Do you want a space between each symbol?'
print 'Enter \'Y\' for yes,\'No\' for no '
choice = raw_input()
number = len(name)
print name
while count <= number:
  if choice == 'y' or choice == 'Y':
    print symbol," "
    count += 2
  else:
    print symbol
    count += 1
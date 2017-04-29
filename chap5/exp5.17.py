# -*- coding:utf-8 -*-
#例5.17使用嵌套循环绘制正方形

print 'Choose a symbol(any character from the keyboard): '
symbol = raw_input()
print 'Enter the length of a side of the square: '
side = input()
count1 = 1
count2 = 1
while count1 <= side:
  while count2 <= side:
    print symbol,
    count2 += 1
  print ''
  count2 = 1
  count1 += 1
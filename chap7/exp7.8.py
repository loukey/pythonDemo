# -*- coding:utf-8 -*-
#例7.8使用ToUpper(),ToLower()函数

print 'Do you want to draw a word-box?Enter \'Y\' or \'N\''
response = raw_input()
while response.upper() == 'Y':
  print 'Enter any word: '
  word = raw_input()
  x = len(word)
  box = word.lower()
  count = 1
  while count<=x:
    print box
    count += 1
  print 'Create a new box? Enter \'Y\' or \'N\''
  response = raw_input()

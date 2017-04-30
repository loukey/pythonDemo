# -*- coding:utf-8 -*-
#例6.6平行数组的串行查找

print 'Enter a student ID number: '
id_key = input()
index = 0
found = 0
id_numbers = [1,2,3,4,5]
names = ['a','b','c','d','e']
scores = [1,2,3,4,5]
n = 2
while found==0 and index<n:
  if id_numbers[index] == id_key:
    found = 1
  index += 1
if found == 0:
  print 'Student ID not found'
else:
  print 'ID Number:',id_key
  print 'Student name:',names[index-1]
  print 'Test score:',scores[index-1]


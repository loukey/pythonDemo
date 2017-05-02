# -*- coding:utf-8 -*-
#例8.7使用数组进行文件维护


student = []
test1 = []
test2 = []

with open('grades.txt','r') as given_file:
  count = 0
  for line in given_file.readlines():
    split_line = line.split()
    student.append(split_line[0])
    test1.append(split_line[1])
    print 'Enter test 2 score for '
    test2.append(raw_input())

with open('grades.txt','w') as data_file:
  for i in range(len(student)):
    data_file.write(student[i])
    data_file.write(' ')
    data_file.write(test1[i])
    data_file.write(' ')
    data_file.write(test2[i])


# -*- coding:utf-8 -*-
#例8.2使用EOF函数

with open('grades.txt','r') as f:
  #先按行读取
  for line in f.readlines():
    #将每一行进行字符串分割
    line_split = line.split()
    student = line_split[0]
    score = line_split[1]
    print student,' ',score


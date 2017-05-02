# -*- coding:utf-8 -*-
#例8.3从顺序文件中删除伪代码
with open('grades.txt','r') as given_file:
  with open('scratch.txt','w') as temp_file:
    print 'Enter name of student to be deleted:'
    delete_name = raw_input()
    for line in given_file.readlines():
      split_line = line.split()
      student = split_line[0]
      score = split_line[1]
      if student!=delete_name:
        temp_file.write(student)
        temp_file.write(' ')
        temp_file.write(score)
        temp_file.write('\n')

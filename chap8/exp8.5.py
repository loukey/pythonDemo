# -*- coding:utf-8 -*-
#例8.5修改顺序文件中指定记录的某个域

with open('grades.txt','r') as given_file:
  with open('scratch.txt','w') as temp_file:
    print 'Enter the name of student:'
    name = raw_input()
    print 'Enter new test score: '
    new_score = str(float(input()))
    for line in given_file.readlines():
      split_line = line.split()
      student = split_line[0]
      score = split_line[1]
      if name==student:
        temp_file.write(name)
        temp_file.write(' ')
        temp_file.write(new_score)
        temp_file.write('\n')
      else:
        temp_file.write(student)
        temp_file.write(' ')
        temp_file.write(score)
        temp_file.write('\n')
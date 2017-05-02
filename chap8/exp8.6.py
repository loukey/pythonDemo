# -*- coding:utf-8 -*-
#例8.6将记录插入到顺序文件中
#书上的例子的意思大概就是这是个按姓名排序的,然后插入到该插入的地方
#我们通过比较字符串的首字符来代替

with open('grades.txt','r') as given_file:
  with open('scratch.txt','w') as temp_file:
    print 'Enter name and score for the new student: '
    new_name,new_score = raw_input(),raw_input()
    inserted = 0
    for line in given_file.readlines():
      split_line = line.split()
      student = split_line[0]
      score = split_line[1]
      if inserted==0:
        if student[0]<new_name[0]:
          temp_file.write(student)
          temp_file.write(' ')
          temp_file.write(score)
          temp_file.write('\n')
        else:
          temp_file.write(new_name)
          temp_file.write(' ')
          temp_file.write(new_score)
          temp_file.write('\n')
          temp_file.write(student)
          temp_file.write(' ')
          temp_file.write(score)
          temp_file.write('\n')
          inserted = 1
      else:
        temp_file.write(student)
        temp_file.write(' ')
        temp_file.write(score)
        temp_file.write('\n')


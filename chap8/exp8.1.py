# -*- coding:utf-8 -*-
#例8.1创建顺序文件
#如果文件不存在就会新建一个文件
#用with可以不用f.close来手动关闭

with open('grades.txt','w') as f:
  print 'Enter the student\'s name and test score'
  print 'Enter 0 for both when done/'
  student = raw_input()
  #写入需要转化成string
  score = str(input())
  while student!='0':
    f.write(student)
    f.write(' ')
    f.write(score)
    f.write('\n')
    print 'Enter the student\' name and test score.'
    print 'Enter 0 for both when done.'
    student = raw_input()
    score = str(input())

# -*- coding:utf-8 -*-
#例5.15每个同学的考试平均成绩
exam_total = 0.0
exam_average = 0.0
print 'Enter a student\' name or enter * to quit:'
name =raw_input()
while name != '*':
  for count in range(1,4):
    print 'Enter exam score number',count
    score = input()
    exam_total += score
  exam_average = exam_total/3
  print 'Student: ',name
  print 'Exam average: ',exam_average
  print 'Enter another student\'s name or enter * to quit: '
  name = raw_input()
  exam_total = 0.0

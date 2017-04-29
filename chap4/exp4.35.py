# -*- coding: utf-8 -*-
#例4.35计算考试平均分
count_grades = 0.0
sum_grades = 0.0
print 'ENter one exam grade. Enter 0 when done.'
grade = input()
while grade>0:
  count_grades += 1
  sum_grades += grade
  print 'Enter an exam grade.Enter 0 when done.'
  grade = input()
exam_average =sum_grades/count_grades
print 'Your exam average is',exam_average
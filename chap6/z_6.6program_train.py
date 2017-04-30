# -*- coding:utf-8 -*-
#6.6问题求解:成绩管理系统



def welcome_message():
  pass

def enter_info():
  student_count = 0
  names = []
  id_num = []
  final = []
  print 'Enter this student\' full name;enter * when done.'
  print 'Use the form \'LastName,FirstName\' for each entry.'
  student_name = raw_input()
  while student_name != '*':
    names.append(student_name)
    student_id = input()
    id_num.append(student_id)
    print 'Enter the final score for this student:'
    student_score = float(input())
    final.append(student_score)
    student_count += 1
    print 'Enter another student\'s name; enter * when done.'
    student_name = raw_input()
  grade = letter_grade(student_count,names,id_num,final)
  display_student(student_count, id_num, names, final, grade)
  statistics(student_count, final, id_num, names, grade)

def letter_grade(student_count,names,id_num,final):
  grade = []
  for i in range(student_count):
    student_score = final[i]
    if student_score>=90.0:
      grade.append('A')
    elif student_score>=80.0:
      grade.append('B')
    elif student_score>=70.0:
      grade.append('C')
    elif student_score>=60.0:
      grade.append('D')
    else:
      grade.append('F')
  return grade

def display_student(student_count,id_num,names,final,grade):
  found = 0
  j = 0
  print 'Enter the ID number for one student to'
  print 'view all the information about that student:'
  id_key = input()
  while found==0 and j<student_count:
    if id_num[j]==id_key:
      found=1
    j += 1
  if found==0:
    print 'Student ID was not found.'
  else:
    print 'Student name:',names[j-1]
    print 'Student ID number:',id_num[j-1]
    print 'Student\'s final score:',final[j-1]
    print 'Student\'s letter grade',grade[j-1]

def statistics(student_count,final,id_num,names,grade):
  flag = 0
  while flag==0:
    flag = 1
    for k in range(student_count-2):
      if final[k]<final[k+1]:
        temp_final = final[k]
        final[k] = final[k+1]
        final[k+1] = temp_final
        temp_id = id_num[k]
        id_num[k] = id_num[k+1]
        id_num[k+1] = temp_id
        temp_name = names[k]
        names[k] = names[k+1]
        names[k+1] = temp_name
        temp_grade = grade[k]
        grade[k] = grade[k+1]
        grade[k+1] = temp_grade
        flag = 0
  high_score = final[0]
  low_score = final[-1]
  sum = 0
  num_above = 0
  num_below = 0
  num_avg = 0
  k = 0
  while k<student_count:
    sum += final[k]
    k += 1
  class_avg = sum/student_count
  for k in range(student_count):
    if final[k]>class_avg:
      num_above += 1
    else:
      if final[k]<class_avg:
        num_below += 1
      else:
        num_avg += 1
  #这里书上写错了,应该是\t
  print 'Student Name \t ID Number \t Final Score \t Letter Grade'
  for k in range(student_count):
    print names[k],'\t',id_num[k],'\t',final[k],'\t',grade[k]
  print 'The average score for this class is:',class_avg
  print 'High score for the class:',high_score
  print 'Low score for the class:',low_score
  print 'Number of scores above the average: ',num_above
  print 'Number of scores below the average: ',num_below
  print 'Number if scores equal to the average: ',num_avg

welcome_message()
enter_info()
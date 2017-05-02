# -*- coding:utf-8 -*-
#例8.8大合并:合并两个文件
#意思就是两个按序排列的文件进行合并,合并后还是按序排列

def read(f):
  line = f.readline()
  #判断一下是否读到结束了
  if line:
    line_split = line.split()
    number = line_split[0]
    name = line_split[1]
    rate = line_split[2]
  else:
    number = 0
    name = ''
    rate = ''
  return number,name,rate

def write(file3,number,name,rate):
  file3.write(number)
  file3.write(' ')
  file3.write(name)
  file3.write(' ')
  file3.write(rate)
  file3.write('\n')

with open('payroll1.txt','r') as file1:
  with open('payroll2.txt','r') as file2:
    with open('payroll.txt','w') as file3:
      number1,name1,rate1 = read(file1)
      number2,name2,rate2 = read(file2)
      while number1!=0 and number2!=0:
        if number1<number2:
          write(file3,number1,name1,rate1)
          number1, name1, rate1 = read(file1)
        else:
          write(file3,number2,name2,rate2)
          number2, name2, rate2 = read(file2)
      while number1!=0:
        write(file3,number1, name1, rate1)
        number1, name1, rate1 = read(file1)
      while number2!=0:
        write(file3,number2, name2, rate2)
        number2, name2, rate2 = read(file2)






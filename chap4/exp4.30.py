# -*- coding: utf-8 -*-
#例4.30使用Int()函数进行数据验证
#忘了备注了,在python里的^号是异或的作用
while True:
  print 'Enter an integer:'
  my_square = input()
  if int(my_square) == my_square:
    break
for count in range(1,my_square+1):
  print count," ",count*count
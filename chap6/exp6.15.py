# -*- coding:utf-8 -*-
#例6.15对字符数组使用length_of函数


print 'Enter a name in the following form: firstname lastname:'
full_name = raw_input()
count = 0
#这里需要大家把名字初始化一下
full_name = [' ' for i in range(30)]
first_name = [' ' for i in range(30)]
last_name = [' ' for i in range(30)]
while full_name[count] != ' ':
  first_name[count] = full_name[count]
  count += 1
first_initial = full_name[0]
last_initial = full_name[count+1]
j = 0
for k in range(count+1,len(full_name)-1):
  last_name[j] = full_name[k]
  j += 1
print last_name,', ',first_name
print 'Your initials are ',first_initial,last_initial
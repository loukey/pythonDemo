# -*- coding: utf-8 -*-
#例4.5巧妙地使用前置测试循环结构
print 'Enter the name of your brother or sister:'
print 'Enter the word Done to quit.'
name = raw_input()
while name != 'Done':
  print name
  name = raw_input()

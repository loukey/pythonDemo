# -*- coding: utf-8 -*-
#例3.1如果你有孩子,说Yes......如果没有,说No

print 'Do you have any children?'
response = raw_input()
if response == 'Y':
  print 'How many?'
  number_children = input()
print 'Questionnaire is complete. Thank you'
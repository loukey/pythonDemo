#-*- coding:utf-8 -*-

import re

pattern = re.compile(r'hello')

result1 = re.match(pattern,'hello')
result2 = re.match(pattern,'helloo CQC!')
result3 = re.match(pattern,'helo CQC !')
result4 = re.match(pattern,'hello CQC!')

if result1:
  print result1.group()
else:
  print '1匹配失败！'

if result2:
  print result2.group()
else:
  print '2匹配失败!'

if result3:
  print result3.group()
else:
  print '3匹配失败'

if result4:
  print result4.group()
else:
  print '4匹配失败'


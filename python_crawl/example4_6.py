#-*- coding:utf-8 -*-

import re
pattern = re.compile(r'(\w+)(\w+)')
s = 'i say, hello world!'
print re.sub(pattern,r'\2\1',s)
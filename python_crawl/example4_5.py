# -*- coding:utf-8 -*-

import re

pattern = re.compile(r'\d+')
for iter in re.finditer(pattern,'one1two2three3four4'):
  print iter.group()
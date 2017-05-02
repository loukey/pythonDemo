# -*- coding:utf-8 -*-
#例7.16递归方案
#小心栈溢出,试试sum(1000)

def sum(n):
  if n == 1:
    return 1
  return n + sum(n - 1)

print sum(5)
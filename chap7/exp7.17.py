# -*- coding:utf-8 -*-
#例7.17使用递归法求数的N次方值

def power(x,n):
  if n==1:
    return x
  return power(x,n-1)*x

print pow(5,3)
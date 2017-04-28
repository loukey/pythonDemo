# -*- coding: utf-8 -*-
#例3.12很长的形式确定等级

print 'Enter Score:'
score = input()
if score==10:
  rating = 'A'
if score==8 or score==9:
  rating = 'B'
if score==6 or score==7:
  rating = 'C'
if score>=1 and score<=5:
  rating = 'D'
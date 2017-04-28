# -*- coding: utf-8 -*-
#例3.13以嵌套if-Then-Else的形式确定等级

print 'Enter Score:'
score = input()
if score==10:
  rating = 'A'
else:
  if score==8 or score==9:
    rating = 'B'
  else:
    if score==6 or score==7:
      rating = 'C'
    else:
      rating = 'D'
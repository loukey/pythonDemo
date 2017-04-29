# -*- coding:utf-8 -*-
#例5.20训练3：高级

a = 1
print 'Cheers! '
while a<3:
  c = a
  print a
  b = 1
  while b<4:
    c += a
    print c
    if a==1 and c>=4:
      print 'Let\'s do this some more! '
    else:
      if a==2 and c>=8:
        print 'Who do we appreciate?'
    b += 1
  a += 1

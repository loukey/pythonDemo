# -*- coding:utf-8 -*-
#例7.9请小心参数传递

def secret_login(part1="",part2=""):
  temp = part1
  part1 = part2.lower() + '**'
  part2 = temp.lower()
  login = part1+part2
  print 'Your secret login is: ',login

print 'Do you want to start?Enter \'yes\' or \'no\': '
response = raw_input()
while response == 'yes':
  print 'Enter this member\'s first name: '
  first = raw_input()
  print 'Enter this member\'s last name: '
  last = raw_input()
  secret_login(first,last)
  print 'Member name: ',first," ",last
  print 'Enter another member? '
  response = raw_input()
  response = response.lower()


# -*- coding: utf-8 -*-
#例1.10 字符串变量的连接

#input()接收输入和raw_input()接收输入不同
#input():当接收字符串输入时,你必须把它放在''中,不然就会当成是变量
#raw_input():所有输入都变成字符串

print 'Enter the person \' first name:'
FirstName = raw_input()
print 'Enter the person\'s last name'
LastName = raw_input()
Fullname = LastName+','+FirstName
print 'The person\'s full name is:',Fullname
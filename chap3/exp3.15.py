# -*- coding: utf-8 -*-
#例3.15使用case语句编写祝福语程序
#其实在python中还有其他的代替case的用法,简单的可以用dictionary,复杂的需要配合lambda表达式～

print 'Enter your favorite whole number between 1 and 5'
fortune = input()
result = {
  1:'You will get a lot of money soon.',
  2:'You will marry your one true love.',
  3:'Study hard! There might be pop quiz tomorrow.',
  4:'Be kind to your teacher.',
  5:'Someday you will become a computer programmer.'
}[fortune]
print result
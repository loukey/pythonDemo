# -*- coding:utf-8 -*-

import urllib2
import cookielib
'''
cookie = cookielib.CookieJar()
#创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#构建opener
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
  print 'Name = ',item.name
  print 'Value = ',item.value
'''
'''
filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
'''
'''
cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
req = urllib2.Request('http://www.baidu.com')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
'''


# -*- coding:utf-8 -*-
import urllib2
req = urllib2.Request('http://neu.edu.cn')
response = urllib2.urlopen(req)
html = response.read()
print html
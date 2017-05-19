# -*- coding:utf-8 -*-

#http://www.qiushibaike.com/hot/page/1

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
headers = {'User-Agent':user_agent}
try:
  request = urllib2.Request(url,headers=headers)
  response = urllib2.urlopen(request)
  content = response.read().decode('utf-8')
  pattern = re.compile(r'<div.class="content".*?>.*?<span>(.*?)</span>',re.S)
  items = re.findall(pattern,content)
  i = 0
  #有很多图读取不了
  for item in items:
    print i
    i += 1
    print item


except urllib2.URLError,e:
  if hasattr(e,'code'):
    print e.code
  if hasattr(e,'reason'):
    print e.reason

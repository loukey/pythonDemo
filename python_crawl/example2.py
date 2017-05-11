# -*- coding:utf-8 -*-

import urllib
import urllib2
#下面是校园网控制网关
#https://ipgw.neu.edu.cn/srun_portal_pc.php?url=&ac_id=1
data={}
data['url']=''
data['ac_id'] = 1
url_values = urllib.urlencode(data)
url = 'https://ipgw.neu.edu.cn/srun_portal_pc.php'
url = url+'?'+url_values
req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()
print html
 - 简介
 	 - 爬虫就是用`http`请求网页,然后网页返回页面信息的一种技术.
 	 - `HTTP`:每一次请求建立一次连接,是一种`TCP/IP`协议形式
 	 - 要掌握好爬虫技术需要会一点web前端知识,会python的语法,正则表达式和xpath基础.`这些我们之后都会讲到.`
 	
 - `example1`
 	 - python用来进行爬虫的最基本的库`urllib`和`urllib2`
 	 - `example1.py`
 	 
 	 		# -*- coding:utf-8 -*-
			import urllib2
			req = urllib2.Request('http://neu.edu.cn')
			response = urllib2.urlopen(req)
			html = response.read()
			print html
	 - 第一步先发送一个request请求到`http://neu.edu.cn`
	 - 第二步接收从官网的反馈
	 - 第三步为读取`response`里的内容
	 - 最后打印得到html页面元素信息

- `example2`:请求
	 - `get`和`post`请求的区别:
	 	 - `get`:表示所有的请求信息都是可见的,例如`http://xxx?name=aaa&password=bbb`,会以`?xxx&xxx&xxx`的形式显示在`url`上
	 	 - `post`:表示相关的请求信息是不可见的,例如上面的`?name=aaa&password=bbb`就会不见了
	 - `example2`
	 	 - `get`:

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
			
- `example3`:Cookie的使用
     - Cookie:网站存储在用户本地的相关信息,例如你登陆一次之后下一次访问页面就不用再重复登陆了
     - Opener:我们可以使用urlopen,但只能传入3个参数(url,data,timeout),当要传入Cookie时,我们需要用到urllib2中更一般的opener
     - Cookielib:CookieJar->FileCookieJar->MozilaCookieJar | LWPCookieJar  (用于存储Cookie的类)
     - 获取Cookie保存到变量
     
     		# -*- coding:utf-8 -*-
            import urllib2
            import cookielib
    
            cookie = cookielib.CookieJar()
            #创建cookie处理器
            handler = urllib2.HTTPCookieProcessor(cookie)
            #构建opener
            opener = urllib2.build_opener(handler)
            response = opener.open('http://www.baidu.com')
            for item in cookie:
              print 'Name = ',item.name
              print 'Value = ',item.value
     - 将cookie保存到本地文件
     
     		# -*- coding:utf-8 -*-
            import urllib2
            import cookielib     
            
            filename = 'cookie.txt'
            cookie = cookielib.MozillaCookieJar(filename)
            handler = urllib2.HTTPCookieProcessor(cookie)
            opener = urllib2.build_opener(handler)
            response = opener.open('http://www.baidu.com')
            cookie.save(ignore_discard=True,ignore_expires=True)
     - 从文件中获取Cookie并访问
          
     		# -*- coding:utf-8 -*-
            import urllib2
            import cookielib  
            
            cookie = cookielib.MozillaCookieJar()
            cookie.load('cookie.txt',ignore_expires=True,ignore_discard=True)
            req = urllib2.Request('http://www.baidu.com')
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
            response = opener.open(req)
            print response.read()
- `example4`:正则表达式简介
	 - 正则表达式表<img src="../img/正则表达式.png"/>
	 - 接下来介绍Python的Re模块对正则表达式的支持
         - re.compile(string[,flag])返回pattern对象
         - re.match(pattern,string[,flags])
         - re.search(pattern,string[,flags])
         - re.split(pattern,string[,maxsplit])
         - re.findall(pattern,string[,flags])
         - re.finditer(pattern,string[,flags])
         - re.sub(pattern,repl,string[,count])
         - re.subn(pattern,repl,string[,count])
     - 解释:
        - `pattern = re.compile(r'hello')`
        - flags表示匹配模式,使用|来表示同时生效,例如`re.I|re.M`
             - re.I(GNORECASE):忽略大小写
             - re.M(ULTILINE):多行模式,改变'^'和'$'的行为
             - re.S(DOTALL):点任意匹配模式,改变'.'的行为
             - re.L(OCALE):使预定字符类\w \W \b \B \s \S取决于当前区域的设定
             - re.U(NICODE):使预定字符类\w \W \b \B \s \S \d \D取决于unicode定义的字符属性
             - re.X(VERBOSE):详细模式.这个模式下正则表达式可以是多行,忽略空白字符,并可以加入注释
		- re.match(pattern,string[,flags]):这个方法将会从字符串的开头开始匹配,当遇到无法匹配或者到达string尾部时还没有匹配结束,都会返回None,否则匹配pattern成功并且终止.
		     - 例子详见example4_1.py
	    - re.search(pattern,string[,flags]):这个方法是搜索整个字符串进行匹配
	         - 例子详见example4_2.py
	    - re.split(pattern,string[,maxsplit]):将字符串进行分割,其中maxsplit为最大分割的次数
	         - 例子详见example4_3.py
	    - re.findall(pattern,string[,flags]):以列表形式返回全部能匹配的子串
	         - 例子详见example4_4.py
	    - re.finditer(pattern,string[,flags]):搜索所有匹配的并且以迭代器的形式返回
	         - 例子详见example4_5.py
	    - re.sub(pattern,repl,string[,count]):使用pattern来匹配字符串,用repl声明的规则来改变字符串
	         - 例子详见example4_6.py
	    - re.subn(pattern,repl,string[,count]):执行re.sub(pattern,repl,string[,count])并加上替换次数
	         - 例子详见example4_7.py

 - example5:实战爬取静态网页`http://www.qiushibaike.com/hot/page/1`
 	 - 用到的正则表达式:
 	 	 - ()表示里面是我们要匹配的东西,用group()来取出
 	 	 - .*?表示最小的匹配,即非贪婪的匹配
 	 	 - re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符
     - 例子详见example5
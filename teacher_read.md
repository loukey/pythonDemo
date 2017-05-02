>书里有一些代码用python实现出现了点问题.
 
 - `python`里没有`switch-case`,可以有3种方法实现:
 	 - 使用dictionary`{'a':case1,'b':case2}`
 	 - 使用`lambda`表达式`{'a':lambda x:x+1,'b':lambda x:x+2}`
 	 - 在底层自己实现一下,我用了`__iter__`,`yield`迭代实现的,代码里都有
 - `python`没有`do-while`和`while-until`,这个实现比较简单,用`while True`和`if-break`
 
 - 书里面有很多`for i=0 ; i<n ;i++`的循环,`python`里都是使用for i in range(n)实现的
 - 书里有`2^3`表示2的3次方,`python`里是用`2**3`实现的,而`^`在`python`里是异或的意思
 - 书里的随机数random,`python`需要使用`import random`模块实现,还有其他一些模块在使用里要引用的,我在代码里都引用了
 - 书上有一些错误,除了拼写错误之外还有`\t`代表一个制表符,书上写反了,写的是`/t`
 - `一个很重大的问题`:在`python`里的形参为传值还是传址的问题,`python`里可变的变量都是传址的,不可变的都是传值的,而第七章的例子很多都是手动改变,`python`不能手动改变
 - python里的输入有两种`input()`和`raw_input()`,前者是输入数字的,后者是输入`string`的
 - 数组,`python`的list不能直接初始化长度,所以和书上实现不太一样
 - 递归,`python`的递归需要return函数体,即实现闭包的方法实现的,和书上不太一样
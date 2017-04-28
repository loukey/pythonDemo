# -*- coding:utf-8 -*-
#例2.8在一个简短的程序中使用分步注释

#python不需要声明变量类型
#这种不需要初始化声明变量类型的叫做弱类型,还有强类型是要初始化的,
# 有趣的是在Objective-C中还有强弱指针,有兴趣的可以了解一下
print 'What are the length and width of the room in inches?'
#获取尺寸大小
length_inches = input()
width_inches = input()
#将尺寸由英寸转化为英尺
length_feet = float(length_inches)/12
width_feet = float(width_inches)/12
#计算平方英尺
square_feet = width_feet *length_feet
#输出结果
print 'Your room is',square_feet,'square feet'
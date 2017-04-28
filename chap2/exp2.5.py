# -*- coding: utf-8 -*-
#例2.5输入和输出模块细化后的伪代码
#因为我不习惯使用变量时首字母大写(帕斯卡命名规范)的,所以这之后我就按照some_some式命名规则来
#驼峰式: someSomeSome(一般JAVA,Swift,Objective-C用的多...)
#some_some式: 忘了叫什么名字了,一般我在C,C++,Python,Golang用的多
#还有全小写的一种,我在写JavaScript的时候会使用这种


#Input
print 'What is the item\'s name?'
item_name = raw_input()
print 'What is its price and the percentage discounted?'
original_price = input()
discount_rate = input()
#Perform Calculations module
amount_saved = original_price*(discount_rate/100)
sale_price = original_price-amount_saved
tax = sale_price*0.065
total_price = sale_price+tax
#Output
print 'The item is:',item_name
print 'Pre-sale price was:',original_price
print 'Sale price:',sale_price
print 'Sales tax:',tax
print 'Total:$',total_price

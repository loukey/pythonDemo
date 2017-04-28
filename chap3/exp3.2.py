# -*- coding: utf-8 -*-
#例3.2盈利还是亏损:if-Then-Else结构

print 'Enter total cost:'
cost = input()
print 'Enter total revenue:'
revenue = input()
amount = revenue-cost
if amount>0:
  profit = amount
  print 'The profit is $',profit
else:
  loss = -amount
  print 'The loss is $',loss
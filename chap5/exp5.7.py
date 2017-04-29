# -*- coding:utf-8 -*-
#例5.7统计邮寄费用
#python官方据说建议用elif代替case,所以在不能用dictionary的情况下,就用这种

item_total = 0
total_cost = 0
print 'How many items are you buying?'
num_items = input()
for count in range(1,num_items+1):
  print 'Enter the cost of item ',count
  item_cost = input()
  if item_cost<=20.00:
    item_cost *= 0.90
  elif item_cost<=50.00:
    item_cost *= 0.85
  elif item_cost<=100.00:
    item_cost *= 0.80
  elif item_cost >100.00:
    item_cost *= 0.75
  item_total += item_cost
if item_total <= 20.00:
  ship = 5.00
elif item_total <= 50.00:
  ship = 8.00
elif item_total <= 100.00:
  ship = 10.00
elif item_total > 100.00:
  ship = 0.0
tax = item_total * 0.06
total_cost = item_total + tax + ship
print 'Your item total is $',item_total
print 'Shipping costs will be $',ship
print 'The total amount due,including sales tax.'
print 'is $',total_cost

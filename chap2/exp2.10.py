# -*- coding:utf-8 -*-
#例2.10伪代码和流程图的对比
#和例2.6的差不多

def input_data_module():
  print 'What is the item\'s name?'
  item_name = raw_input()
  print 'What is its price'
  original_price = input()
  print 'What is the percentage discounted?'
  discount_rate = input()
  return item_name,original_price,discount_rate

def calculations_module():
  item_name, original_price, discount_rate = input_data_module()
  amount_saved = original_price*(discount_rate/100)
  sale_price = original_price-amount_saved
  tax = sale_price*0.065
  total_price = sale_price+tax
  return item_name,original_price,discount_rate,sale_price,tax,total_price

def results_module():
  item_name, original_price, discount_rate, sale_price, tax, total_price = calculations_module()
  print 'The item is:',item_name
  print 'Pre-sale Price was:$',original_price
  print 'Percentage discounted was:',discount_rate,'%'
  print 'Sale price:$',sale_price
  print 'Sales tax:$',tax
  print 'Total cost now is:$',total_price

print 'Sale Price Program'
print 'This program computes the total price, including tax,of'
print 'an item that has been discounted a certain percentage.'
print 'a certain percent'
results_module()

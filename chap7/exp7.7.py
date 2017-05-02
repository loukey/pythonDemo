# -*- coding:utf-8 -*-
#例7.7售价计算程序之再设计

def welcome_message():
  print 'This program is a sale price calculator.'
  print 'When you enter the original price of an item and how much'
  print 'it has been discounted, the program will display the'
  print 'original price, the discount rate, and the new sale price.'

def input_data(price,rate):
  print 'Enter the price of an item: '
  price = float(input())
  print 'Enter the percentage it is discounted:'
  rate = float(input())
  return price,rate

def compute_results(orig_price,dis_rate):
  amount_saved = orig_price*dis_rate/100
  sale = orig_price-amount_saved
  return sale

def output_results(old_price,rate,new_price):
  print 'The original price of item is $',old_price
  print 'The discount is: ',rate,'%'
  print 'The sale price of the item is $',new_price

price = 0.0
rate = 0.0
sale = 0.0
welcome_message()
price,rate = input_data(price,rate)
sale=compute_results(price,rate)
output_results(price,rate,sale)
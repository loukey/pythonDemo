# -*- coding: utf-8 -*-
#4.5问题求解:成本、收入和盈利问题

def welcome_message():
  pass

def input_data():
  while True:
    print 'Enter the number of desired production levels.'
    print 'It must be an integer greater than or equal to 1'
    num_rows = input()
    if int(num_rows)==num_rows and num_rows>=1:
      break
  return  num_rows

def display_table():
  welcome_message()
  num_rows = input_data()
  return num_rows

def table_housekeeping():
  print 'KingPin Manufacturing Company'
  print 'Number Cosot Revenue Profit'
  num_rows = display_table()
  spacing = int(1000/num_rows)
  return spacing,num_rows

def table_computation():
  spacing,num_rows = table_housekeeping()
  sum = 0
  for x in range(spacing,1001,spacing):
    cost = 100000+12*x
    revenue = x*(1000-x)
    profit = revenue-cost
    sum += profit
    print x," ",cost," ",revenue," ",profit
  return sum,num_rows

def display_average():
  sum,num_rows = table_computation()
  average = sum/num_rows
  print 'The average profit is',average

display_average()


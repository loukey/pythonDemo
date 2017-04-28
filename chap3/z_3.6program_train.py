# -*- coding: utf-8 -*-
#3.6问题求解:新车价格计算器

def compute_engine_cost():

  result = False
  while not result:
    print 'S - 6 cylinder engine'
    print 'E - 8 cylinder engine'
    print 'D - Diesel engine'
    print 'Selection?'
    engine_choice = raw_input()
    result = {'S':150,'E':475,'D':750,}[engine_choice] if engine_choice=='S'or'E'or'D' else False
    if not result:
      print 'Invalid selection'

  return result  #result === engine_cost

def compute_interior_cost():

  result = False
  while not result:
    print 'V - vinyl interior trim'
    print 'C - Cloth interior trim'
    print 'L - Leather interior trim'
    print 'Selection?'
    trim_choice = raw_input()
    result = {'V':50,'C':225,'L':800,}[trim_choice] if trim_choice=='V'or'C'or'L' else False
    if not result:
      print 'Invalid selection'

  return result  #result ===trim_cost

def compute_radio_cost():

  print 'R - AM/FM/CD/DVD Radio'
  print 'D - add GPS'
  print 'Selection?'
  radio_choice = raw_input()
  radio_cost = 100 if radio_choice=='R' else 400

  return radio_cost

def display_selling_price(base_price):
  engine_cost = compute_engine_cost()
  trim_cost = compute_interior_cost()
  radio_cost = compute_radio_cost()
  shipping_charge = 500
  dealer_charge = 175
  selling_price = base_price + engine_cost + trim_cost + radio_cost + shipping_charge + dealer_charge
  print 'The total selling price for your vehicle is $',selling_price

#main module
print 'Enter the base price: '
base_price = input()
display_selling_price(base_price)
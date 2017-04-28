# -*- coding: utf-8 -*-
#例3.7加班还是没加班

pay_rate = input()
hours = input()

if pay_rate<10 and hours>40:
  overtime_hours = hours-40
  overtime_pay = overtime_hours*1.5 * pay_rate
  total_pay = 40*pay_rate + overtime_pay
else:
  total_pay = hours*pay_rate
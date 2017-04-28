# -*- coding: utf-8 -*-
#例3.8加班还是没加班(修订版)

pay_rate = input()
hours = input()

if pay_rate>=10 or hours<=40:
  total_pay = hours * pay_rate
else:
  overtime_hours = hours-40
  overtime_pay = overtime_hours * 1.5 * pay_rate
  total_pay = 40 * pay_rate + overtime_pay
  
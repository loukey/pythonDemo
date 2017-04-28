# -*- coding: utf-8 -*-
#例3.18Legendary Lawn Mower公司的存货清单

print '    The Legendary Lawn Mower Company'
print '                     Inbentory Control'
print '  Leave th program................Enter 0'
print 'Add an item to the list...........Enter 1'
print 'Delete an item from the list......Enter 2'
print 'Change an item on the list........Enter 3'
print '         Selection-->'
choice = input()
result = {
  0:'Goodbye',
  1:'AddItem module',
  2:'DeleteItem module',
  3:'ChangeItem module'
}[choice]

print result
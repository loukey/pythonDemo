# -*- coding:utf-8 -*-
#例9.6使用OOP来解决停车难问题

class person():
  def __init__(self):
    self.name = ''
    self.city = ''
    self.age = 1.0
    self.vehicle = ''

  def set_name(self,new_name):
    self.name = new_name

  def set_city(self,new_city):
    self.ci1 = new_city

  def set_age(self,new_age):
    self.age = new_age

  def set_travel(self,new_vehicle):
    self.vehicle = new_vehicle

  def get_name(self):
    return self.name

  def get_city(self):
    return self.city

  def get_age(self):
    return self.age

  def get_travel(self):
    return self.vehicle

class faculty(person):
  def __init__(self):
    person.__init__(self)
    self.subject = 1
    self.parking_lot = 1

  def set_subject(self,new_subject):
    self.subject = new_subject

  def get_subject(self):
    return self.subject

  def compute_parking_lot(self,new_subject):
    self.parking_lot = new_subject
    return self.parking_lot

class student(person):

  def __init__(self):
    person.__init__(self)
    self.subject = 1.0
    self.parking_lot = 1.0

  def set_subject(self,new_subject):
    self.subject = new_subject

  def get_subject(self):
    return self.subject

  def compute_parking_lot(self,new_subject):
    self.parking_lot = new_subject+5
    return self.parking_lot

prof_one = faculty()
print 'What\'s the profeesor\'s name?'
prof_name = raw_input()
prof_one.set_name(prof_name)
print 'What type of car does this professor drive?'
prof_car = raw_input()
prof_one.set_travel(prof_car)
print 'What is the professior\'s general subject area?'
print 'Enter 1 for Lib'
print 'Enter 2 for Engineering & Computer Science'
print 'Enter 3 for Health & Medicine'
print 'Enter 4 for Business'
print 'Enter 5 for Education'
prof_subject = input()
prof_one.set_subject(prof_subject)
prof_lot = prof_one.compute_parking_lot(prof_subject)
print 'Professor',prof_one.get_name(),';'
print 'You may park your',prof_one.get_travel()
print 'in Parking lot',prof_lot
stu_one = student()
print 'What is student\' name? '
stu_name = raw_input()
stu_one.set_name(stu_name)
print 'What type of bike does this student have?'
stu_bike = raw_input()
stu_one.set_travel(stu_bike)
print 'What is the student\'s major?'
print 'Enter 1 for Loberal Arts'
print 'Enter 2 for Engineering & Computer Science'
print 'Enter 3 for Health & Medicine'
print 'Enter 4 for Business'
print 'Enter 5 dor Education'
stu_subject = input()
stu_lot = stu_one.compute_parking_lot(stu_subject)
print 'Student',stu_one.get_name(),":"
print 'You may park your',stu_one.get_travel()
print 'in Parking Lot',stu_lot
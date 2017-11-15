#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
 
   stuCount = 0
 
   def __init__(self, stu_no,name,stu_class,male):
      self.name = stu_no
      self.name = name
      self.stu_class = stu_class
      self.male = male
      Student.stuCount += 1
   
   def displayCountByClass(self):
     print "Total Employee %d" % Student.stuCount
 
   def displayEmployee(self):
      print "Stu_no : ",self,stu_no,",self.name", self.name,  ", Stu_class,",self.male

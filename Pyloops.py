#!/usr/bin/python

class Employee:
	"Common base class for all employees"
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name : ", self.name, ", Salary: ", self.salary

"Create first object in employee class"
emp1 = Employee("Zara", 2000)
"Create 2nd obj employee"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.emp.Count  
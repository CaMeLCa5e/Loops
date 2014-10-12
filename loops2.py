#loops 2

for letter in 'Python':
	print 'Current Letter:' , letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
	print 'Current fruit : ', fruit 
	
print 'Good bye!'

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
	print 'Current fruit:', fruits [index]
	
print 'Good bye!'




for x in 'Python':
	print "Letter - ", x
	
for num in range(10, 20):
	for i in range(2,num):
		if num%i == 0:
			j=num/i
			print 'd% equals %d * %d' % (num, i, j)
			break 
	else:
		print num, 'is a prime number'
'''		
a = 0
while a > 10:
	a = a + 1
	print a
'''

x = 10 
print 'counting down'
while x != 0:
#	print x
	x=x -1
	print '', x
print 'blast off!!!!!'



a = 10
while a > 0:
	print a
	if a > 5:
		print 'Big number'
	elif a %2 != 0:
		print 'This is an odd number'
		print  'less than five'
	else: 
		print 'this number isn\'t greater than 5'
		print 'not is it odd'
	a = a - 1
	print 'we just made "a" one less than what it was'
	print 'and unless it is not greater than 0, do the loop again'
print 'end'



























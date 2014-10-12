#loops 3 

for letter in 'Python':
	if letter == 'h':
		break
	print 'current letter:', letter
	
	
print "----------------new example "

var = 10
while var > 0:
	print 'current variable value:', var
	var = var -1
	if var ==5:
		break 
		
print 'end'


print 'new ex--------------------- continue statement'

for letter in 'Python':
	if letter == 'h':
		continue
	print 'current letter ;', letter
	
	
print 'new ex'
###############################

var = 10 
while var > 0:
	var = var -1	
	if var == 5:
		continue
	print 'current variable value :' , var
print 'Good Bye'

###############################

for num in range (10, 20):
	for i in range (2, num):
		if num%i == 0:
			j=num/i
			print '%d equals %d * %d' % (num, i, j)
			break 
	else:
		print num, 'is prime baby!'
###############################

for letter in 'Python':
	if letter == 'h':
		pass
		print 'This is a pass block'
	print 'Current Letter:', letter

print 'Later!'

###############################

x = -20 
y = 20 
while x <= y:
	print 'x is now:', x
	x = x +1
	while x <= 0:
		print "x is negative! -  ", x
		x = x + 1

###############################
count = 0 
while count < 10:
	print 'The current count is:', count
	count += 1
else:
	print "The final count is:", count

names  = ['Bill', 'Jack', 'Pumba']
for x in names:
	print x 






#####################




countries = []

count = 0

while count < 5: 
	print "please enter a country that you have been to"
	next = raw_input ("> ")
	if len (next) > 0 and next.isalpha():
		countries.append(next)
		count = count + 1
	else:
		print "I am sorry, I cannot accept that input"
print "You have been to these countries!"
print countries




















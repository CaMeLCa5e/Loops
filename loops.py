#loops. lots of loops 

for count in [1,2,3,]:
	print(count)
	print ('Yes' * count)
	
for count in [1,2,3]:
	print (count)
	print ('Yes' * count)
print ('Done counting.')
for color in ['red', 'blue', 'green']:
	print (color)
	
for count in [1,2,3]:
	print count
	print 'yes'* count
	print 'Done counting.' 
for color in ['red', 'blue', 'green']:
	print color
	
#for cue in ['animal', 'food', 'city']:
#	addPick (cue, userPicks)

def numberList(items):
	number = 1
	for item in items:
		print (number, item)
		number = number +1
		
def main():
	numberList(['red', 'orange', 'yellow', 'bananas'])
	print()
	numberList (['apples', 'pears', 'bananas'])
		
main()


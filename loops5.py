#loops5

colors = ['red']
for i in colors:
	if i == 'red':
		colors += ['black']
	if i == 'black':
		colors += ['white']
print colors

# all the colors get printed in above example- side effects...  

colors =['red']
for i in colors [:]:
	if i == 'red':
		colors += ['black']
	if i == 'black':
		colors += ['white']
print colors


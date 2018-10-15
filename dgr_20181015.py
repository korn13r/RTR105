# Conditional steps
x = 5
if x < 10:
	print('Smaller')
	if x > 20:
		print('Bigger')
		print ('Finish')

		
# Comparison operators
x = 5
if x == 5:
	print('Equals 5')
	if x > 4:
		print('Greater than or Equals 5')
		if x < 6:
			print('Less than or Equals 5')
			if x != 6:
				print('Not Equals 6')


# one way decisions				
x = 5
print('Before 5')
if x == 5:
	print('Is 5')
	print('Is Still 5')
	print('Third 5')
	print('Afterwards 5')
	print('Before 6')
	if x == 6:
		print('Is 6')
		print('Is Still 6')
		print('Third 6')
		print('Afterwards 6')

		
x = 5
if x > 2:
	print('Bigger than 2')
	print('Still bigger')
	print('Done with 2')

	
x = 5
if x > 2:
	print('Bigger than 2')
	print('Still bigger')
	print('Done with 2')
	for i in range(5):
		print(i)
		if i > 2:
			print('Bigger than 2')
			print('Done with i',i)
			print('All Done')


# Nested decisions
x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All Done')


# two way decisions with 'else'
x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')


#  Multi-way
x = 0
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
    print('All done')





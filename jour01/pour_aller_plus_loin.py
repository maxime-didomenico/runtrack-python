string=str(input('enter a string: '))
char=str(input('enter a character: '))

if char in string :
	print('\033[92m' + char, 'is in the string.')
else:
	print('\033[31m' + char, 'is not in the string.')

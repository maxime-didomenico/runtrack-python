import random
from random import choice

i=0

for i in range(0,25):
	x = chr(ord('z') - i)
	j=random.randint(1,9)
	print('\033[3{}m'.format(j) +  x, end='')
else:
	x = chr(ord('z') - (i + 1))
	print(x)

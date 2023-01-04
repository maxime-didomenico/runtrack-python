def pyramide(nb):
	alph = "abcdefghijklmnopqrstuvwxyz"
	index = 0
	i = 0
	j = 0
	while (i < nb):
		while (j <= i):
			if index == 26:
				index = 0
			else:
				print(alph[index], end='')
				index+=1
				j+=1
		i+=1
		j = 0
		print(' ')

pyramide(10)	

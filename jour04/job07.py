L = [8, 24,48,2,16]

def tcount(list):
	i = 0
	while i < len(list):
		if ((list[i] % 3) == 0):
			print(list[i])
			i+=1
		else:
			i+=1

tcount(L)

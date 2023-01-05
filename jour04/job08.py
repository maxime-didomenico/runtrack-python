L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

def oddc(list):
	i = 0
	sum = 0
	while i < len(list):
		if ((list[i] % 2) == 0):
			sum+=list[i]
			i+=1
		else:
			i+=1
	print(sum)

oddc(L)

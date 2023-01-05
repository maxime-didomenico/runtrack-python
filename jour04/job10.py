L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def prodl(list):
	i = 0
	sum = 1
	while i < len(list):
		if list[i] >= 25 and list[i] <= 90 :
			sum*=list[i]
			i+=1
		else:
			i+=1
	print(sum)

prodl(L)

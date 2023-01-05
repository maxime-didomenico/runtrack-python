L = [7, 11, 42, 39, 2]

def oddc(list):
	i = 0
	while i < len(list):
		list[i]+=1
		i+=1
	return(list)

print(oddc(L))

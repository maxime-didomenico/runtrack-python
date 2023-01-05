L = [1,2,3,4,5]

def replace(list):
	swap = list[len(list) - 1]
	list[len(list) - 1] = list[0]
	list[0] = swap
	return(list)

print(L)
print(replace(L))

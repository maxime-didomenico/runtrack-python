def ft_len(list):
	count = 0
	for i in list:
		count+=1
	return(count)

def tri(list):
	i = 0
	while i < ft_len(list) - 1:
		if list[i] > list[i + 1]:
			swap = list[i + 1]
			list[i + 1] = list[i]
			list[i] = swap
			i = 0
		else:
			i+=1
	return(list)

L = [7, 11, 42, 39, 2]
print(tri(L))
L = [90, 19, 17, 30, 0]
print(tri(L))

print(len(L))
print(ft_len(L))

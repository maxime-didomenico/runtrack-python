L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def maxmin(list):
	print("max = ",max(list))
	print("min = ",min(list))

def minlong(list):
	min = list[0]
	i = 1
	while i < len(list):
		if (list[i] < min):
			min = list[i]
			i+=1
		else:
			i+=1
	return(min)

def maxlong(list):
	max = list[0]
	i = 1
	while i < len(list):
		if (list[i] > max):
			max = list[i]
			i+=1
		else:
			i+=1
	return(max)

maxmin(L)
print("------------------")
print("min = ",minlong(L))
print("max = ",maxlong(L))

def job():
	i = int(1)
	while (i < 101):
		if (i%3) == 0 and (i%5) == 0:
			print(i, end='')
			print("fizzbuzz")
			i+=1
		elif (i%3) == 0:
			print(i, end='')
			print("fizz")
			i+=1
		elif (i%5) == 0:
			print(i, end='')
			print("buzz")
			i+=1
		else:
			i+=1

job()

def pyth(a, b, c):
	if a > b and a > c:
		cotes=(c*c + b*b)
		hyp=(a*a)
		if cotes == hyp:
			return 0
		else:
			return 1
	elif b > a and b > c:
		cotes=(c*c + a*a)
		hyp=(b*b)
		if cotes == hyp:
			return 0
		else:
			return 1
	elif c > a and c > b:
		cotes=(a*a + b*b)
		hyp=(c*c)
		if cotes == hyp:
			return 0
		else:
			return 1

def triangle(a, b, c):
	if a == b and b == c and c == a:
		print("Ceci est un triangle equilateral.")
	elif a == b or b == c or c == a:
		print("Ceci est un triangle isocele.")
		if pyth(a,b,c) == 0:
			print("Cependant ce triangle possède également un angle droit, le rendant rectangle.")
	else:
		print("Ce triangle est quelconque.")
		if pyth(a,b,c) == 0:
			print("Mais ce triangle possède également un angle droit, le rendant rectangle.")

print("Triangle de mesure : 1 1 1")
triangle(1,1,1)
print("Triangle de mesure : 2 2 1")
triangle(2,2,1)
print("Triangle de mesure : 5 4 3")
triangle(4,3,5)

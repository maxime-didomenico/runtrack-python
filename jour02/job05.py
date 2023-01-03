def calcul(num1, ope, num2):
	if ope == "+":
		res = num1 + num2
	if ope == "-":
		res = num1 - num2
	if ope == "/":
		res = num1 / num2
	if ope == "%":
		res = num1 % num2
	return(res)

print(calcul(5, '+', 1))
print(calcul(5, '-', 1))
print(calcul(5, '/', 2))
print(calcul(5, '%', 2))

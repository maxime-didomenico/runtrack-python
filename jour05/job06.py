def starwars(grade):
	if grade < 40:
		print(grade," your failed the force is not with you.")
	elif grade >= 40:
		if grade % 5 >= 3 or grade % 5 == 0:
			new_grade = grade
			while new_grade % 5 != 0:
				new_grade+=1
			print(new_grade,"you succeed with the force.")
		else:
			new_grade = grade
			print(new_grade," you succeed but not with the force.")

starwars(5)
starwars(5)
starwars(82)
starwars(83)
starwars(100)
starwars(99)

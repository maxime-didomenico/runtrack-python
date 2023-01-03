def courses(type, saison):
	if type == "fruits" and saison == "hiver":
		print("orange, mandarine et kiwi")
	elif type == "fruits" and saison == "ete":
		print("Poire, fraise et cassis")
	elif type == "legumes" and saison == "hiver":
		print("carotte, topinambour et endive")
	elif type == "legumes" and saison == "ete":
		print("artichaut, aubergine et navet")
	else:
		print("je ne compwen pas")

courses("fruits", "hiver")
courses("fruits", "ete")
courses("legumes", "hiver")
courses("legumes", "ete")
courses("tomates", "automne")

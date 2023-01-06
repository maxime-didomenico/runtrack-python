def flemme(x,y):
	dist = x * y # trajet d'un aller
	dist *= 2 # aller + retour
	dist *= 5 # trajet par jour
	dist *= 7 # trajet par semaine
	dist /= 100 # conversion en m 
	return(dist)

print(flemme(183,10), " mètres par semaine.")

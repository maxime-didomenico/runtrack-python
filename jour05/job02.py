def print_line(lenght, side_char, top_char):
	print(side_char, end='')
	if lenght > 1:
		i = 0
		while i < lenght - 2:
			print(top_char, end='')
			i+=1
		print(side_char)

def draw_rectangle(x,y,side_char,top_char):
	if x >= 1 and y >= 1:
		print_line(x,side_char,top_char)
		if y > 1:
			i = 0
			while i < y - 2:
				print_line(x,side_char,' ')
				i+=1
			print_line(x,side_char,top_char)

draw_rectangle(10,10,'o','-')

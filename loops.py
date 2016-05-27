#def countFrom2(x, y):
#	if x > y:	
#		while x >= y:
#			print x
#			x -= 1
#	elif y > x:		
#		while x <= y:
#			print x
#			x += 1

#countFrom2(23, 20)
#countFrom2(2, 20)


#def addOdds():	
#	if m > 0:
#	elif m < 0:
		

def grid(w,h):
	out = ""
	x = 0	
	while x < w:
		out += "."
		x += 1
	return out

print grid(10,5)

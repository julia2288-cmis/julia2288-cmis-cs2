print "This  program will ask you for 5 integer or float values. It will calculate the average of all valus from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd."

def numbers():
	float(n0) = raw_input("n0: ") 
	if float(n0) >= float(10):
		print "{} is out of range.".format(float(n0))
	elif float(n0) < float(0):
		print "{} is out of range.".format(float(n0))
	else:
		return True

	n1 = raw_input("n1: ") 
	if n1 >= float(10):
		print "{} is out of range.".format(n1)
	elif n1 < float(0):
		print "{} is out of range.".format(n1)
	else:
		return True

	n2 = raw_input("n2: ") 
	if n2 >= float(10):
		print "{} is out of range.".format(n2)
	elif n2 < float(0):
		print "{} is out of range.".format(n2)
	else:
		return True

	n3 = raw_input("n3: ") 
	if n3 >= float(10):
		print "{} is out of range.".format(n3)
	elif n3 < float(0):
		print "{} is out of range.".format(n3)
	else:
		return True

	n4 = raw_input("n4: ") 	
	if n4 >= float(10):
		print "{} is out of range.".format(n4)
	elif n4 < float(0):
		print "{} is out of range.".format(n4)
	else:
		return True

numbers()



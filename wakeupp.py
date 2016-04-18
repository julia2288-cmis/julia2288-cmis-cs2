print "This  program will ask you for 5 integer or float values. It will calculate the average of all valus from 0 inclusive to 10 exclusive. It will print out whether the resulting average is even or odd."

def numbers():
	n0 = raw_input("n0: ") 
	n1 = raw_input("n1: ") 
	n2 = raw_input("n2: ") 
	n3 = raw_input("n3: ") 
	n4 = raw_input("n4: ") 	

numbers()

def define(numbers):
	if numbers >= float(10):
		print "{} is out of range.".format(numbers)
	else:
		return True

define(numbers)

def average(numbers):
	average = float(number0 + number1 + number2 + number3 + number4 / 5)
	return """
The average is {}.
The interger part of the average is {}.
""".format()

average(numbers):

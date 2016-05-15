import random

def rules():
	print "This is just like snakes and ladders. If you press enter, computer will roll the dice. You have to go forward with the given number. There will be some traps in few steps.Good luck!"

def steps():	
	n = raw_input("Click enter to roll the dice.")	
	float(dice) = random.randint(1,6) 
	if n == "":
		return float(dice)
	print "You are in number {}.".format(float(dice))
	c = raw_input("Type enter to continue: ")
	elif c == "":
		return steps() 

def traps1():
	n = steps()
	if n == float(6,13,39,69)
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps()


def traps2():
	n = steps()
	if n == float(9,26,73,81)
		print "You stepped on a banana peel. You will slip 3 steps back." 
		return abs(float(sub(n-3)))


def traps3():
	n = steps()
	if n == float(28,43,96)
		print "You found an escalator infront of you. You will skip 4 steps to the front."
		return abs(float(add(n+4)))

import random

def rules():
	print "This is just like snakes and ladders. If you press enter, computer will roll the dice. You have to go forward with the given number. There will be some traps in few steps.Good luck!"

def steps(dice):	
	dice = raw_input("Click enter to roll the dice.")	
	if dice == "":
		return random.randint(1,6) 
	print "You are in number {}.".format(dice)
	
def next(c):
	c = raw_input("Type enter to continue: ")	
	if c == "":
		return steps(dice) 

def traps1():
	n = steps(dice)
	if n == float(6,13,39,69,70,24,36,99,4,14):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(dice)


def traps2():
	n = steps(dice)
	if n == float(9,26,33,35,21,2,73,81,65):
		print "You stepped on a banana peel. You will slip 3 steps back." 
		return abs(float(sub(n-3)))


def traps3():
	n = steps(dice)
	if n == float(28,43,58,62,10,96,7,34,23,78):
		print "You found an escalator infront of you. You will skip 4 steps to the front."
		return abs(float(add(n+4)))

def main():
	steps(dice)
	n = steps(dice)
	if n == float(100):
		print "You won!"
	
main()

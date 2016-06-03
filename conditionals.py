import random
import math

print "This is just like snakes and ladders. If you press enter, computer will roll the dice. You have to go forward with the given number. There will be some traps in few steps. Good luck!"
	
def steps(total):		
	dice = raw_input("Click enter to roll the dice.")	
	if dice == "":
		print
		n = random.randint(1,6)	
		print n
		total += int(n)
		out = """
"You are in number {}.
""".format(total)	
		print out
		return total


def traps():
	total = steps(0)

	if total == float(1):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(0)
		return steps(total)


	elif total == float(5):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(total+4))
		return steps(total)

	elif total == float(6):
		print "You found an U.F.O, you will transfer to a random place."
		return steps(random.random*10)
		return steps(total)

	elif total == float(52):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(0)
		return steps(total)

	elif total == float(84):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(0) 
		return steps(total)

	
def traps2():
	
	if total == float(3):
		print "You stepped on a banana peel. You will slip 3 steps back." 
		return abs(float(total-3))
		return steps(total)

	elif total == float(28):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(total+4))
		return steps(total)
	
	elif total == float(8):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(total+4))
		return steps(total)
	
	elif total == float(78):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(total+4))
		return steps(total)
	
	elif total == float(38):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(total+4))
		return steps(total)
	
	elif total == float(32):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(total+4))
		return steps(total)
	
	else:
		return steps(total)


def end(total):
	steps(0)
	if total >= 100 :
		return True
	else:
		return False
		
def main():
	traps()
	total = steps(0)
	
	if total == 50:
		print "Half way!"
	
	else: 
		total == 90 or total > 90
		print "Almost there!"

main()


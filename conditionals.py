import random
import math

def rules():
	print "This is just like snakes and ladders. If you press enter, computer will roll the dice. You have to go forward with the given number. There will be some traps in few steps.Good luck!"

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
	total= steps(total)
	if total == float(1):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(total)

	if total == float(5):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(total)

	if total == float(6):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(total)

	if total == float(52):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(total)

	if total == float(84):
		print "You stepped on a snake and the snake bite you. You will start from the beginning again."
		return steps(total)

	elif total == float(3):
		print "You stepped on a banana peel. You will slip 3 steps back." 
		return abs(float(sub(total-3)))

	elif total == float(28):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(add(total+4)))
	
	elif total == float(8):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(add(total+4)))
	
	elif total == float(78):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(add(total+4)))
	
	elif total == float(38):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(add(total+4)))
	
	elif total == float(32):
		print "You found an escalator in front of you. You will skip 4 steps to the front."
		return abs(float(add(total+4)))
	

def main():
	total = steps(0)
	traps()
	if total == 50:
		print "Half way!"
	
	elif total >= 90:
		print "Almost there!"

	else:
		total >= 100
		return steps(total)

main()


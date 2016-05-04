def countdown(n):
	if n <= 0:
		print "Blastoff!"
	else:
		print n
		countdown(n-1)


def countup(n):
	if n >= 0:
		print "Blastoff!"
	else:
		print n
		countup(n+1)

def countup_from_to(start, stop):
	if start >= stop:
		print "Blastoff!"
	else:
		print start
		countup(start+1)

def countdown_from_to(start, stop):
	if start <= stop:
		print "Blastoff!"
	else:
		print start
		countdown(start-1)

def adder(total):
	print "The running total is {}".format(running_total)
	n = raw_input("next number: ")
	if n == "":
		print "bye"
	else:
		running_total += float(n0)
		adder(running_total)

def biggest(big):
	 

def main():

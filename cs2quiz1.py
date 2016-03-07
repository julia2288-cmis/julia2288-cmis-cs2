#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# That is called assignment operator, and it's used for putting a value into a variable.
#+1
#
#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statements that performs a computation.
#+3
#
#3 1pt) What does the keyword "return" do?
# It takes the function and gives a result.
#+1
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: interger
#	2: float
#	3: strings
#	4: boolean
#	5: tuple
#+2.5

#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# Function deifnition specifies(in other word, defines) the new function, and function call is actualling calling the function that has been specified. 
#+1
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1: programming languages
#	2: compiled
#	3: interpreted
#1

#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi


import math
def float(a, r):
	return a / r**2 / pi 


def output():
	out = """
circle	diameter
c1:	{}
c2:	{}
c3:	{}
total:	{}
""". format()
	return out


def main():
	A = raw_input("What is the area for c1?: ")
	B = raw_input("What is the area for c2?: ")
 	C = raw_input("What is the area for c3?: ")
	area = mult(float(r), float(2))
	out = output(area, A, pi, r)
	print out 

main()
# area = pi * radius^2
# a / pi / = x
# x / x = radius
# radius * 2 = diameter

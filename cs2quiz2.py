#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) a == a
#b) 3 > 2
#c) True != False
# +3
#
#2) What does 'return' do?
# It takes the function and gives a result.
#
#
#
#
#3) What are 2 ways indentation is important in python code?
#a)It is important because python uses indentation to define a block
#b)
#
#

#PART 2: Reading
#Type the values for 9 of the 12 of the variables below.
#
#problem1_a) (36)
#problem1_b) (3)
#problem1_c) (0)
#problem1_d) (-5)

#problem2_a)
#problem2_b)
#problem2_c)
#problem2_d)
#
#problem3_a)
#problem3_b)
#problem3_c)
#problem3_d)
#0.5
#problem4_a)
#problem4_b)
#problem4_c)
#problem4_d)
#a + b or (2, 3, 4) + (3, 2, 1)

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

def float(A, B, C):
	if A > B and C:
		return A
	
	elif B > A and C:
		return B

	elif C > B and A: 
		return C

	else:
		return "You must type different numbers."

def main():
	raw_input("Type 3 different numbers (decimals are OK!) ")
	raw_input(float(A: ))
	raw_input(float(B: ))
	raw_input(float(C: ))

main()

def mult(m,a):
	return m * a
#Defines the critical functions.

def output(m, a, F):
	out = """
The force you want to find is:
{} = {} * {}
""". format(F, m, a,)
	return out
#Defines the output.

def main():
	m = raw_input("What is the mass?")
	a = raw_input("What is the acceleration?") 
	F = mult(float(m), float(a))
	out = output(m, a, F)
	print out
	print "Here is the answer!"
main()
#Defines the main fuction. 

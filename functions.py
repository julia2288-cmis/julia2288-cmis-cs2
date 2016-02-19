import math
def add(a, b):
	return a+b
x=add(3, 4)
print x
# this adds number a and b

def sub(a, b):
	return a-b
y=sub(5, 3)
print y
# this subtracts a and b

def mul(a, b):
	return a*b
w=mul(4, 4)
print w
# this multiplies a and b

def div(a, b):
	return a/b
	return float
z=div(2.0, 3)
print z
# this divides a and b

def hours_from_seconds (a):
	return a / 3600
print hours_from_seconds (86400)
# this turns a into hours

def circle_area (a):
	return math.pi * (a**2)
print circle_area (5)
#A function that tells the area of a circle

def sphere_volume (a):
	return 1.33333333333 * math.pi * (a**3)
print sphere_volume (5)
#A function that tells the volume of a sphere

def avg_volume (a, b):
	 return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2
print avg_volume(10, 20)
#A function that tells the average voulume of two spheres

def area (a, b, c):
	return math.sqrt (2.75*(2.75-a)*(2.75-b)*(2.75-c))
print area (1.0, 2.0, 2.5)
#A function that tells the area of a triangle

def right_align(a):
	return (a.rjust(80))
right_align("Hello")
#A function that aligns hello to the right side of python

def center(a):
	return (a.center(40))
center("Hello")
#A function that aligns hello to center of python

def msgbox(a):
	x =    """		  +---------+
		  |  """+"Hello"+"""  |
		  +---------+"""
	print x
	return"""		  +---------------+
		  |  """+"I eat cats!"+"""  |
		  +---------------+"""
	
print msgbox("")

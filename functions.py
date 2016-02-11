import math 
def add(a,b):
	return a + b	
print add(3,4)
#addition
def sub(a,b):
	return a - b
print sub(5,3)
#subtaction
def mul(a,b):
	return a * b
print mul(4,4)
#multiplication
def div(a,b):
	return a / float(b)
print div(2,3)
#division
def hours_from_seconds(a,b,c):
	return a / b / c
print hours_from_seconds(86400,60,60)
#number of seconds and returns the number of hours.
def circle_area(a):
	return math.pi*a**2
print circle_area(5)
#adius of a circle.
def sphere_volume(v):
	return (((4/3.0)*math.pi)*v**3)
print sphere_volume(5)
# radius of a sphere and returns the volume.
def avg_volume(

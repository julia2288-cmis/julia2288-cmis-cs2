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
# A fuction that turns seconds into hours

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
    return "+" + (len(a) + int(4)) * "-" + "+\n" "|" + "  " + a + "  " + "|\n" "+" + (len(a) + int(4)) * "-" + "+"
msgbox("Hello")
msgbox("I eat cats")
print msgbox("Hello")
print msgbox("I eat cats")
#Message box of "hello" and "I eat cats"

a = add(4,6)
b = add(8,6)
print msgbox(str(a))
print msgbox(str(b)) 
# this adds number a and b

c = sub(5,3)
d = sub(4,4)
print msgbox(str(c))
print msgbox(str(d)) 
# this subtracts c and d

e = mul(2,3.0)
f = mul(4,8)
print msgbox(str(e))
print msgbox(str(f)) 
# this multiplies e and f

g = div(48,8)
h = div(625,25)
print msgbox(str(g))
print msgbox(str(h)) 
# this divides g and h

i = hours_from_seconds(46890,60,60)
j = hours_from_seconds(60000,60,60)
print msgbox(str(i))
print msgbox(str(j)) 
# this turns seconds into hours

k = circle_area(6)
l = circle_area(9)
print msgbox(str(k))
print msgbox(str(l)) 
# tells the area of a circle

m = sphere_volume(7)
n = sphere_volume(14)
print msgbox(str(m))
print msgbox(str(n)) 
#tells the volume of a sphere

o = avg_volume(20,40)
p = avg_volume(40,60)
print msgbox(str(o))
print msgbox(str(p)) 
# tells the average voulume of two spheres

q = area(2,2,2)
r = area(4,2,6)
print msgbox(str(q))
print msgbox(str(r)) 
#tells the area of a triangle

s = right_align("MEEEEE")
t = right_align("The end is nigh!")
print msgbox(str(s))
print msgbox(str(t)) 
#aligns hello to the right side of python

u = center("Haundig")
v = center("Who wants to play CSGO?")
print msgbox(str(u))
print msgbox(str(v)) 
#aligns hello to center of python

w = msgbox("Dragons dogma")
x = msgbox("Undertale")
print msgbox(str(w))
print msgbox(str(x)) 
#aligns hello to center of python

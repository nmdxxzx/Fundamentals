#Use type() to check a variable's type
#You get SyntaxError when your variable is a number, has illegal characters or is one of Python's keywords.
#Example of illegal variables: 17, ^n, class


import math
from turtle import*

n = int(input("Please enter the radius of circle?"))
print("area of circle is", math.pi*n**2 )

Celsius = int(input("Enter the temperature in Celsius?"))
Farenheit = (Celsius - 32)*5/9
print(Celsius, "(C) =", Farenheit, "(F)" )
type(n)

print(type(n))

shape("turtle")
speed(0)
for i in range(4):
    forward(100)
    left(90)
for i in range(3):
    right(120)
    forward(100)
for i in range(12):
    for i in range(360):
        forward(math.pi*2*n/360)
        left(1)



z = input("")
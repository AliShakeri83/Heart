import math
from turtle import *

def Heart_a(n):
    return 15 * math.sin(n) ** 3

def Heart_b(n):
    return 12 * math.cos(n)-5 *\
        math.cos(2*n) -2 *\
        math.cos(3*n) - \
        math.cos(4*n)
        
tracer(2)

bgcolor("black")

for i in range(8000):
    goto(Heart_a(i)*15, Heart_b(i)*15)
    for j in range(1):
        color('red')
        hideturtle()
        goto(0,0)

done()
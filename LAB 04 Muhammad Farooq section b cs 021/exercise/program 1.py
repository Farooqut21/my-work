#1. Write a program which solves the quadratic equation. The user will enter the value of a, b and c. The program will then check the denominator that if denominator is zero or not. If its zero it can reply the equation cannot solve as there is a zero division else, it will execute the program and will generate two solutions.  
import cmath
a=int(input("enter your number"))
b=int(input("enter your number"))
c=int(input("enter your number"))
d=b**2-4*a*c
sol_1=(-b-cmath.sqrt(d))/2*a

sol_2=(-b+cmath.sqrt(d))/2*a
print("the two solutions are:",sol_1,sol_2)

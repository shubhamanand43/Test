"""
7. Design and develop a program in a language of your choice to solve the
Triangle problem defined as follows: Accept three integers which are supposed
to be the three sides of a triangle and determine if the three values represent
an equilateral triangle, isosceles triangle, scalene triangle, or they do not
form a triangle at all. Derive test cases for your program based on decision-table
approach, execute the test cases and discuss the results.

"""

print("Enter 3 integers which are sides of triangle")

a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

print(f"A = {a} , B = {b} , C = {c}")

# to check is it a triangle or not

if( a < b+c and b < a+c and c < a+b ):
    istriangle ='y'
else:
    istriangle ='n'

if (istriangle=='y'):
    if ((a==b) and (b==c)):
        print("Equilateral triangle")
    elif ((a!=b) and (a!=c) and (b!=c)):
        print("Scalene triangle")
    else:
        print("Isosceles triangle")
else:
    print("Not a triangle")

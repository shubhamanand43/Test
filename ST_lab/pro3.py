"""
3.
Design, develop, code and run the program in any suitable language to
implement the NextDate function. Analyze it from the perspective of
boundary value testing, derive different test cases, execute these test cases
and discuss the test results.

"""

month = [31,28,31,30,31,30,31,31,30,31,30,31]
print("Enter the date,month,year")

d = int(input("Enter dd : "))
m = int(input("Enter mm : "))
y = int(input("Enter yyyy : "))


if(y<=1812 and y>2012):
    print("Invalid Input Year")
    exit()

if(m<1 and m>12):
    print("Invalid Input Month")
    exit()

ndays = month[len(month)-1]

if(d<=0 or d>ndays):
    print("Invalid Input Day")
    exit()

if(m==2):
    if(y%100==0):
        if(y%400==0):
            ndays=29
    elif(y%4==0):
        ndays=29
nd=d+1
nm=m
ny=y

if(nd>ndays):
    nd=1
    nm += 1

if(nm>12):
    nm=1
    ny += 1
print(f"\nGiven date is {d}:{m}:{y}")
print(f"\nNext day date is {nd}:{nm}:{ny}")

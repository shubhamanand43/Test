"""
6. Design, develop, code and run the program in any suitable language to implement
the Next Date function. Analyze it from the perspective of equivalence class value
testing, derive different test cases, execute these test cases and discuss the
test results.

"""

month = [31,28,31,30,31,30,31,31,30,31,30,31]
print("Enter the Date, Month, Year")

d = int(input("Enter dd : "))
m = int(input("Enter mm : "))
y = int(input("Enter yyyy : "))
flag = 0

if(y<=1812 or y>2100):
    print("Invalid Input Year!")
    flag = -1

if(m<1 or m>12):
    print("Invalid Input Month!")
    flag = 1

if flag != 1:
    ndays = month[m-1]

if(m==2):
    if(y%100==0):
        if(y%400==0):
            ndays=29
    elif(y%4==0):
            ndays=29

if flag == 1:
    print("Day Can't be Checked as Month is not appropriate")
else:
    if(d<=0 or d>ndays):
        print("Invalid Input Day!")
        flag = -1

if flag==0:
    nd=d+1
    nm=m
    ny=y

    if(nd>ndays):
        nd=1
        nm += 1

    if(nm>12):
        nm=1
        ny += 1

    if 1<=d<=9:
        d = "0" + str(d)
    if 1<=m<=9:
        m = "0" + str(m)
    print(f"Given date is : {d}-{m}-{y}")
    if 1<=nd<=9:
        nd = "0" + str(nd)
    if 1<=nm<=9:
        nm = "0" + str(nm)
    print(f"Next day date is : {nd}-{nm}-{ny}")

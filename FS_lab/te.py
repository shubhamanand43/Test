print("Enter DD MM YYYY")
d = int(input())
m = int(input())
y = int(input())

if(y <= 1812 or y > 2012):
    print("Invalid Input Year")
    exit()

if(m < 1 or m > 12):
    print("Invalid Input Month")
    exit()

if((y <= 1812 or y > 2012) and (m < 1 or m > 12)):
	print("Invalid Input Month and Year")


if(y%4==0 and y%100!=0 or y%400==0):
    print('leap year')
    b=29
else:
    print('not a leap year')
    b=28
month=[31,b,31,30,31,30,31,31,30,31,30,31]
ndays = month[m-1];
if(d <= 0 or d > ndays):
    print("Invalid Input Day")
    exit()

if(m == 2):
    if(y%4==0 and y%100!=0 or y%400==0):
    	ndays=29


nd = d + 1
nm = m
ny = y

if(nd > ndays):
    nd=1
    nm = nm + 1


if(nm > 12):
    nm = 1
    ny = ny + 1


print("Given date is ",d,m,y);
print("Next day is date is ",nd,nm,ny);

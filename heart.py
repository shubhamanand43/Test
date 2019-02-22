zt = " "
st = "*"

n = int(input("Enter Odd Number : "))
m = 2*n-1

o = int(n/2 + 1)

for i in range(int(n/2 + 1),n,2):
    print(zt*int(o/2-1) + st*i + zt*(o-1) + st*i)
    o -= 2
#print(o)
for i in range(1,n+1):
    print(zt*(i-1) + st*m)
    m -= 2

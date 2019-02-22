
# Read(r)
# Write(w)
# Update(u)
# Search(s)

def write():

    n = int(input("Enter How Many Record you want to store : "))
    for i in range(0,n):

        name = input("Enter Name : ")
        usn = input("Enter USN : ")
        sub = input("Enter Marks : ")
        print("\n")

        try:
            f = open(file="student.txt",mode='a')
                zt = " "
                st = a + "|" + b + "|" + c + "|"
                m = (40 - len(st))
                rs = st + zt*m + "\n"
            f.write(rs)
        finally:
            f.close()

def read():
    pass

def search():
    pass

def update():
    pass

while run == True:
    s = input("Enter 'r' for READ , 'w' for WRITE , 's' for SEARCH , 'u' for UPDATE : ")
    if(s == "r"):
        read()
    elif( s == "w"):
        write()
    elif( s == "s"):
        search()
    elif( s == "u"):
        update()
    else:
        run = False

#
# n = int(input("Enter How Many Record you want to store : "))
#
# def setline(a,b,c):
#     zt = " "
#     st = (a + zt*(20 - len(a))) + "|" + (b + zt*(12 - len(b))) + "|" + (c + zt*(10 - len(c)))
#     m = (50 - len(st))
#     return st + zt*m + "\n"
#
# for i in range(0,n):
#
#     name = input("Enter Name : ")
#     usn = input("Enter USN : ")
#     sub = input("Enter Marks : ")
#     print("\n")
#
#     try:
#         f = open(file="student.txt",mode='w')
#         f.write(setline(name,usn,sub))
#
#     finally:
#         f.close()

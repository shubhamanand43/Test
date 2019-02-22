n = int(input("Enter How Many Record you want to store : "))

# Read
# Write
# Update
# Search

def setline(a,b,c):
    zt = " "
    st = a + "|" + b + "|" + c + "|"
    m = (50 - len(st))
    return st + zt*m + "\n"

for i in range(0,n):

    name = input("Enter Name : ")
    usn = input("Enter USN : ")
    sub = input("Enter Marks : ")
    print("\n")

    try:

        f = open(file="student.txt",mode='a')
        f.write(setline(name,usn,sub))

    finally:
        f.close()

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

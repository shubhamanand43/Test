
# Read(r)
# Write(w) ++
# Update(u)
# Search(s) ++

f = open(file="student.txt",mode='r')
f.seek(0)
st = f.read()
ls = st.split('|')

mls = []
ils = []

for i in range(0, int((len(ls)-1)/5)):
    for j in range(i*5+1, (i+1)*5+1):
        ils.append(ls[j])
    mls.append(ils.copy())
    ils.clear()


#modify
 = input("Enter Name or Usn (Give USN to be SPECIFIC) to Change it : ")
 = input("Enter Name or Usn (Give USN to be SPECIFIC) to Change it : ")
serr = True if ki in ls else False
if serr == True:
    ls[ls.index(ki)] = e
    f = open(file="student.txt",mode='w')
    f.write("")
    f.close()
    for i in range(0,len(mls)):
        name = ls[i*5+1]
        usn = ls[i*5+2]
        marks = ls[i*5+3]
        zt = " "
        st = "|" + name + "|" + usn + "|" + marks + "|"
        rs = st + zt*(40 - len(st)) + "|\n"
        f = open(file="student.txt",mode='a')
        f.write(rs)
        f.close()
else:
    print("CAN'T IDENTYFY RECORD")

#delete


def write():
    n = int(input("Enter How Many Record you want to store : "))
    for i in range(0,n):
        name = input("Enter Name : ")
        usn = input("Enter USN : ")
        marks = input("Enter Marks : ")
        print("\n")

        try:
            f = open(file="student.txt",mode='a')
            f.seek(0,2)
            zt = " "
            st = "|" + name + "|" + usn + "|" + marks + "|"
            rs = st + zt*(40 - len(st)) + "|\n"
            f.write(rs)
        finally:
            f.close()

def read(s,e=0):
    if e == 0:
        lt = ls[s*5:(s+1)*5+1]
    else:
        lt = ls[s*5:e*5+1].copy()
    return " | ".join(lt)

def search(ls,mls):

    sb = input("Enter 'n' for SEARCH BY NAME or 'u' for SEARCH BY USN : ")
    ki = input("Enter keyword to FIND : ")

    def colS(ls, mls, col, ki):
        serc = True if ki in [i[col] for i in mls] else False
        if serc == True:
            f = int(ls.index(ki)/len(mls))
            return f+1
        else:
            print("NOT FOUND")
            return -1

    if sb == 'n':
        ch = colS(ls,mls,0,ki)
    elif sb == 'u':
        ch = colS(ls,mls,1,ki)

    if ch == -1:
        return -1
    else:
        return ch

def update():
    pass

f.close()

# run = True
# while run :
#     s = input("Enter 'r' for READ , 'w' for WRITE , 's' for SEARCH , 'u' for UPDATE and 'q' to QUIT: ")
#     if(s == "r"):
#         sa = int(input("Enter Start line (Can be ZERO, if e = 0 it will give Single Line) : "))
#         ea = int(input("Enter End line for START to END result or For Single Line put '0' : "))
#         print(read(sa,ea))
#     elif( s == "w"):
#         write()
#     elif( s == "s"):
#         m = search(ls,mls)
#         if m == -1: pass
#         else:
#             print(mls[m][:3])
#     elif( s == "u"):
#         update()
#     else:
#         run = False

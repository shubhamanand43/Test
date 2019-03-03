"""
2. Write a program to read and write student objects with fixed-length records and the
fields delimited by “|”. Implement pack ( ), unpack ( ), modify ( ) and search ( )
methods.

"""
# f.seek(0, 0)
# self.ils = []
# for i in range(0, len(self.ls)):
#     self.ils.append(str(i+1) + self.ls[i])

class flr():
    def __init__(self,fn):
        f = open(file=fn,mode='r')
        f.seek(0, 0)
        self.ls = f.readlines()
        f.close()

    def pack(self,nr):
        lp = []
        for i in range(0, nr):
            print("Enter USN, NAME, MARKS, ADDRESS, BRANCH and COLLEGE Respectively ..")
            u = input(" -> ")
            n = input(" -> ")
            m = input(" -> ")
            a = input(" -> ")
            b = input(" -> ")
            c = input(" -> ")
            if len(u)>10 or len(n)>20 or len(m)>3 or len(a)>30 or len(b)>20 or len(c)>20 :
                print("Length Exeeding")
                exit()
            else :
                pk = "|"+u+" "*(10-len(u))+"|"+n+" "*(20-len(n))+"|"+m+" "*(3-len(m))+"|"+a+" "*(30-len(a))+"|"+b+" "*(20-len(b))+"|"+c+" "*(20-len(c))+"|"
                lp.append(pk)
        return lp # Gives |fdgs|FSDGDF|SFDG|SFDG|JKNN|JHBjhNIIO| for 1

    def unpack(self,s,e=9999):
        up = self.ls
        if e >= len(up):
            st = "".join(up[s:])
        else:
            st = "".join(up[s:e])
        upl = st.split("|")
        return upl # Gives ['', '123       ', '1233                ', '12 ', '12334                         ', 'rterterte           ', 'rghghgh             ', '\n'] for 1

    def read(self):
        print("|".join(self.unpack(0)))

    def write(self,fn):
        f = open(file=fn,mode='a')
        f.seek(0, 2)
        nr = int(input("Enter No of Record(s) : "))
        li = self.pack(nr)
        lir = map(lambda x: x+"\n" , li)
        f.writelines(lir)
        f.close()

    def search(self,usn):
        lss = self.unpack(0).copy()
        if usn in list(filter(lambda x : lss.index(x) % 7 == 1 , lss)):
            ix = lss.index(usn)
        else:
            ix = "SEARCH NOT FOUND"
            print(ix)
            exit()
        rn = int((ix-1)/7)
        return rn # Gives index of rows of record as int

    def modify(self,fn,usn):
        sd = {'n' : 2, 'm': 3, 'a': 4, 'b': 5, 'c': 6}
        ld = {'n' : 20, 'm': 3, 'a': 30, 'b': 20, 'c': 20}

        lm = self.ls.copy()
        mt = input("Enter 'n' for Name, 'm' for Marks, 'a' for Address, 'b' for Branch, 'c' for College  CHANGE : ")
        ins = input("Data to Replace -> ")
        if len(ins) > ld[mt]:
            print("Data Entered Greater then FIXED LENGTH")
            exit()
        mo = lm[self.search(usn)]
        mod = mo.split("|")
        mod[sd[mt]] = ins + " "*(ld[mt]-len(ins))
        mo = "|".join(mod)
        lm[self.search(usn)] = mo
        # print(lm)
        f = open(file=fn,mode='w')
        f.seek(0, 2)
        f.writelines(lm)
        f.close()

run = True
fn = input("Enter filename to Process : ")
while(run):
    ch = input("Enter 'r' for Read, 'w' for Write, 's' for Search, 'm' for Modify and 'q' for QUIT : ")
    obj = flr(fn)
    objm = flr(fn)
    if ch == 'r':
        obj.read() # ++
    elif ch == 'w':
        obj.write(fn) # ++
    elif ch == 's':
        usn = input("Enter USN {NOT MORE THEN 10 LETTERS}: ")
        usn = usn + " "*(10-len(usn))
        rn = obj.search(usn)
        print("|".join(obj.unpack(rn,rn+1)))
    elif ch == 'm':
        usn = input("Enter USN {NOT MORE THEN 10 LETTERS}: ")
        usn = usn + " "*(10-len(usn))
        objm.modify(fn,usn)
    elif ch == 'q':
        run = False

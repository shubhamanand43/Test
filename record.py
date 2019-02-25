
# Read(r) ++
# Write(w) ++
# alter(a) ++
# Search(s) ++
# delete(d) ++

class RecordManage():

    # constrctor for initializing file every time new object is made to use some of the Fuctions..
    def __init__(self,fn):
        fc = open(file=fn, mode='r')
        self.st = fc.read()
        # get all the file content in a list.
        self.ls = self.st.split('|')
        fc.close()
        self.mls = []
        ils = []
        # Make a Matrix of DATA Arranged of Above list as a different 2D List.
        for i in range(0, int((len(self.ls)-1)/4)):
            for j in range(i*4+1, (i+1)*4+1):
                ils.append(self.ls[j])
            self.mls.append(ils.copy())
            ils.clear()

    def read(self,ls):
        """ # Read as desired line or desired lines Consecutively Adjecent. """
        s = int(input("Enter Start line (Can be ZERO, if e = 0 it will give Single Line) : ")) # take START index of Line
        e = int(input("Enter End line for START to END result or For Single Line put '0' : ")) # take END index as Exclusive of Line or put '0' to get only 1 record as indexed START.

        if e == 0:
            lt = ls[s*4:(s+1)*4+1].copy() # Copy() Makes Copy of data in a different Mamory location Don't Point to the same.
        else:
            lt = ls[s*4:e*4+1].copy()
        # Returns the list Croped to get the desired Elements.
        return " | ".join(lt)

    def write(self,fn):
        """ # Writes Record(s) using user inputs and append to the Working file. """
        n = int(input("Enter How Many Record you want to store : "))
        for i in range(0,n):
            name = input("Enter Name : ")
            usn = input("Enter USN : ")
            marks = input("Enter Marks : ")
            print("\n")
            # Open as append mode
            f = open(file=fn ,mode='a')
            f.seek(0,2)
            # Makes a record  as a String to Fit in the file.
            st = "|" + name + "|" + usn + "|" + marks + "|"
            rs = st  + "\n"
            f.write(rs)
            f.close()

    def search(self,ls,mls):
        """ # Searchs Record Using Key input As USN or Name. """
        sb = input("Enter 'n' for SEARCH BY NAME or 'u' for SEARCH BY USN : ")
        ki = input("Enter keyword to FIND : ")
        l = ls
        m = mls
        # Func to find out the Where Element Located.
        def colS(ls, mls, col, ki):
            serc = True if ki in [i[col] for i in mls] else False
            if serc == True:
                f = int(ls.index(ki)/4)
                #print(f)
                return f
            else:
                print("NOT FOUND")
                return -1
        # if-else for choosing the SEARCH BY NAME or SEARCH BY USN
        if sb == 'n':
            ch = colS(l,m,0,ki)
        elif sb == 'u':
            ch = colS(l,m,1,ki)

        if ch == -1: pass
        else:
            # Prints list of FOUND Data.
            print(mls[ch][:3])

    def alter(self,ls,mls,fn):
        """ # alter data ie change USN or Name at a time or Change Marks giving USN to Search data. """
        gm = input("Enter 'u' for Change USN or NAME  or 'm' for change marks : ")
        if gm == "u" :
            kin = input("Enter Name or Usn (Give USN to be SPECIFIC) to SEARCH it : ")
            kch = input("Enter Name or Usn (Give USN to be SPECIFIC) to REPLACE it : ")
        elif gm == "m" :
            kin = input("Enter USN  to Change Marks of it : ")
            min = input("Enter Marks : ")

        serr = True if kin in ls else False
        if serr == True:
            # Assigning the or changeing the values according.
            if gm == 'u':
                ls[ls.index(kin)] = kch
            elif gm == 'm':
                ls[ls.index(kin)+1] = min
            # it will clear all data in the file
            f = open(file=fn, mode='w')
            f.write("")
            f.close()
            # Now again rewrite the Modified data.
            for i in range(0,len(mls)):
                name = ls[i*4+1]
                usn = ls[i*4+2]
                marks = ls[i*4+3]
                st = "|" + name + "|" + usn + "|" + marks + "|"
                rs = st + "\n"
                f = open(file=fn, mode='a')
                f.write(rs)
                f.close()
        else:
            print("CAN'T IDENTIFY RECORD")

    def delete(self,ls,mls):
        kin = input("Enter Usn to delete that RECORD : ")

        serr = True if kin in ls else False
        if serr == True:
            l = ls.index(kin)
            del ls[l-1:l+3]
            # it will clear all data in the file
            f = open(file=fn,mode='w')
            f.write("")
            f.close()
            # Now again rewrite the Modified data.
            for i in range(0,len(mls)-1):
                name = ls[i*4+1]
                usn = ls[i*4+2]
                marks = ls[i*4+3]
                st = "|" + name + "|" + usn + "|" + marks + "|"
                rs = st + "\n"
                f = open(file=fn, mode='a')
                f.write(rs)
                f.close()


# Ask to use NEW file or Previous ONE.
askf = input("Enter 'nf' MAKE NEW FILE or 'pf' for USE PREVIOUS FILE : ")
fn = input("Enter file Name : ")
if askf == "nf":
    f = open(file=fn, mode='w')
    f.close()
elif askf == "pf" :
    pass

# All Above Functions all organised to work properly.
run = True
while run == True:
    ch = input("Enter 'r' for READ, 'w' for WRITE, 's' for SEARCH, 'u' for UPDATE and 'q' to QUIT : ")

    if ch == "r":
        rmr = RecordManage(fn)
        print(rmr.read(rmr.ls))

    elif ch == "w":
        rmw = RecordManage(fn)
        rmw.write(fn)

    elif ch == "s":
        rms = RecordManage(fn)
        #print(str(rms.ls) + " \n  " + str(rms.mls))
        rms.search(rms.ls,rms.mls)

    elif ch == "u":
        rmu = RecordManage(fn)
        ud = input("Enter 'd' for DELETE or 'a' for ALTER : ")
        if ud == "a":
            rmu.alter(rmu.ls,rmu.mls,fn)
        elif ud == "d" :
            rmu.delete(rmu.ls,rmu.mls,fn)

    elif ch == "q":
        run = False

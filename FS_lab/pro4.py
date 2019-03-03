"""
4. Write a program to write student objects with Variable - Length records using any
suitable record structure and to read from this file a student record using RRN.

"""
# Insert a record
# Search a record using RNN

class flr():
    def __init__(self,fn):
        f = open(file=fn,mode='r')
        f.seek(0, 0)
        self.ls = f.readlines()
        f.seek(0, 0)
        self.ils = []
        for i in range(0, len(self.ls)):
            self.ils.append(str(i+1) + self.ls[i])
        f.close()

    def pack(self):
        print("Enter USN, NAME, MARKS, ADDRESS, BRANCH and COLLEGE Respectively ..")
        u = input(" -> ")
        n = input(" -> ")
        m = input(" -> ")
        a = input(" -> ")
        b = input(" -> ")
        c = input(" -> ")
        pk = "|"+u+"|"+n+"|"+m+"|"+a+"|"+b+"|"+c+"|"
        return pk

    def insert(self,fn):
        f = open(file=fn,mode='a')
        f.seek(0, 2)
        pk = self.pack() + "\n"
        f.writelines(pk)
        f.close()

    def search(self,rnn):
        ls = self.ils
        if rnn > len(ls):
            sr = "RNN EXEEDS THEN AVAILABLE"
        else:
            sr = ls[rnn-1]
        print(sr)

run = True
fn = input("Enter filename to Process : ")
while(run):
    ch = input("Enter 'i' for Insert a Record or 's' for Search a Record or 'q' for QUIT : ")
    ob = flr(fn)
    if ch == 'i':
        ob.insert(fn)
    elif ch == 's':
        rnn = int(input("Enter RNN {NOT MORE THEN Records in FILE}: "))
        ob.search(rnn)
    elif ch == 'q':
        run = False

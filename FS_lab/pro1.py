"""
1. Write a program to read series of names, one per line, from standard input and write
these names spelled in reverse order to the standard output using I/O redirection and
pipes. Repeat the exercise using an input file specified by the user instead of the
standard input and using an output file specified by the user instead of the standard
output.

"""

def filein(fin):
    li = []
    nr = int(input("Enter the no of Records : "))
    for i in range(0, nr):
        st = input(" -> " )
        li.append(st + "\n")
    fi = open(file=fin, mode='w')
    fi.seek(0, 2)
    fi.writelines(li)

def fileout(fin, fio):
    fo1 = open(file=fin, mode='r')
    fo1.seek(0, 0)
    lo = fo1.readlines()
    lom = list(map(lambda x : x[:len(x)-2] ,lo))
    lor = list(map(lambda x : x[::-1] + "\n" ,lom))
    fo2 = open(file=fio, mode='w')
    fo2.seek(0, 2)
    fo2.writelines(lor)
    fo1.close()
    fo1.close()

def sio():
    si = []
    nr = int(input("Enter the no of Records : "))
    for i in range(0, nr):
        st = input(" -> " )
        si.append(st)
    l = list(map(lambda x : x + "\n" ,si))
    print("Input Data -> \n" + "".join(l))
    lr = list(map(lambda x : x[::-1] + "\n" ,si))
    print("Output Data -> \n" + "".join(lr))

ch = input("Choose 'f' for File I/O or 's' for Standard I/O : ")
if ch == "f":
    fin = input("Enter filename for Input : ")
    fio = input("Enter filename for Output : ")
    filein(fin)
    fileout(fin,fio)
elif ch == "s":
    sio()

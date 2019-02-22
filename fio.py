import os

mode = input("Enter 'r' for Read Or Enter 'w' for Write : ")

try:
    if mode == "w":
        st = input("Write them : ")
        f = open(file="ex1.txt", mode='a')
        f.write(st)
        print(f.tell())
        f.seek(0)
    elif mode == "r":
        f = open(file="ex1.txt", mode='r')
        f.seek(0)
        print(f.read())
finally:
    f.close()

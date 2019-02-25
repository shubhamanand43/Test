"""
10. Design, develop, code and run the program in any suitable language to
implement the binary search algorithm. Determine the basis paths and using them
derive different test cases, execute these test cases and discuss the test results.

"""

a = []
n = int(input("Enter No of Elements : "))
print("Enter Elements ")
for i in range(0,n):
    inp = int(input(" -> "))
    a.append(inp)

ki = int(input("Enter the key to Search : "))

def search(a,ki):
    low = 0
    high = n-1
    key = ki
    flag = 0

    while ( low <= high ):
        mid = int((low + high) / 2)
        if (a[mid] == key):
            print("Successful\n")
            print(f"INDEX OF {key} is : " + str(a.index(key) + 1))
            flag = 1
            exit()

        elif (a[mid] > key ):
            high = mid - 1
        else:
            low = mid + 1

    if flag == 0:
        print("Unsuccessful")

search(a,ki)

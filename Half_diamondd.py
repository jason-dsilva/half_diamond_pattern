r = int(input("enter the number of rows "))
for i in range (r):
    for j in range (0,i+1):
        print("*",end='')
    print()
for i in range (1,r):
    for j in range (i,r):
        print("*",end='')
    print()

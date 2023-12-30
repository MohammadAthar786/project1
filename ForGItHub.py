rows=int(input("Enter rows : "))


for i in range(0,rows):
    for j in range(rows-1-i,0,-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()



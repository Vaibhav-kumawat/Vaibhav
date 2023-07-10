# While loop to making patterns

n = int(input("\n Enter number of rows : "))
row = 1
while row<=n:
    col = 1
    i=n
    while i>row:
        print(" ",end="")
        i-=1
    while col<=row:
        print("*",end=" ")
        col+=1
    print()
    row+=1

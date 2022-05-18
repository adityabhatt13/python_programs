n = int(input())
for i in range(1,n+1):
    for space in range(n-i,0,-1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for k in range(1,i):
        print("*", end="")
    print()            
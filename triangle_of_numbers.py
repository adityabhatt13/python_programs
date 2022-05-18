n = int(input())
for i in range(1,n+1):
    for space in range(n-i,0,-1):
        print(" ", end="")
    for j in range(i,i*2):
        print(j, end="")
    for k in range(i*2-2,i-1,-1):
        print(k, end="")
    print()        
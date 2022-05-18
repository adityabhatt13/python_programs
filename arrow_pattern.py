n = int(input())
for i in range(n//2+1):
    for space in range(i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n//2,0,-1):
    for space in range(i-1):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()        

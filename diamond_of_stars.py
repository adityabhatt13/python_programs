n = int(input())
for i in range(1,n-1):
    for space in range(n-i-2,0,-1):
        print(" ", end="")
    for j in range(0,i):
        print("*", end="")
    for k in range(1,i):
        print("*", end="")
    print()  
for i in range(1,n-2):
    for space in range(1,i+1):
        print(" ", end="")
    for j in range(1,n-i-1):
        print("*", end="")
    for k in range(n-i-2,1,-1):
        print("*", end="")    
    print()              
n = int(input())
for i in range(1,n+1):
    for j in range(i):
        if i > 2 and j > 0 and j < i-1:
            print("0", end="")
        elif i == 1:
            print("1", end="")
        else:    
            print(i-1, end="")
    print()            
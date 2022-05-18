n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if j > 1 and j < i:
            print("2", end="")
        else:
            print("1", end="")
    print()            
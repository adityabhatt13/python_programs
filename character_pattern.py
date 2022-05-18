n = int(input())
for i in range(1,n+1):
    k = i
    for j in range(i):
        print(chr(64+k), end="")
        k += 1
    print()    
        
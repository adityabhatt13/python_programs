n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+n-i+j), end="")
    print()    

n = int(input())
startChar = chr(64+n)
for i in range(1,n+1):
    for j in range(1,i+1):
        print(ord(startChar)-i+j, end="")
    print()        
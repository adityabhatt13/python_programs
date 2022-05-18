n = int(input())
for i in range(0,n,2):
    for j in range(n*i+1,n*(i+1)+1):
        print(j, end=" ")
    print()
if n%2 != 0:
    for i in range(n-2,0,-2):
        for j in range(n*i+1,n*(i+1)+1):
            print(j, end=" ")        
        print()
else:
    for i in range(n-1,0,-2):
        for j in range(n*i+1,n*(i+1)+1):
            print(j, end=" ")        
        print()    
            

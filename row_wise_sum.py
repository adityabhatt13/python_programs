str = input().split()
n,m = int(str[0]),int(str[1])
li = [[int(j)for j in input().split()]for i in range(n)]
for i in range(n):
    sum = 0
    for j in range(m):
        sum = sum + li[i][j]
    print(sum, end =" ")    

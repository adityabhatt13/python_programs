li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(li)
m = len(li[0])
for j in range(m):
    if j%2 == 0:
        for i in range(n):
            print(li[i][j], end=" ")
    else:
        for i in range(n-1,-1,-1):
            print(li[i][j], end=" ")        
nm = [int(x) for x in input().split()]
n,m = nm[0],nm[1]
mat = []
for i in range(m):
    mat.append([x for x in input().split()])          
for li in mat:
    for i in range(n):
        print(" ".join(li))
    n -= 1


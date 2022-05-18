n = int(input())
for i in range(0,n):
    for j in range(n,n-i,-1):
        print(j, end="")
    for k in range(1,n*2-i*2):
        print(n-i, end="")
    for l in range(n-i+1,n+1):
        print(l, end="")
    print()
for i in range(0,n-1):
    for j in range(n,i+1,-1):
        print(j, end="")
    for k in range(i*2+1,0,-1):
        print(i+2, end="")
    for l in range(i+2,n+1):
        print(l, end="")
    print() 


# n=int(input())
# for i in range(1,2*n):
#     k=n
#     for j in range(1,2*n):
#         print(k, end="")
#         if j<i:
#             k=k-1
#         if j>=2*n-i:
#             k=k+1
#     print("")            
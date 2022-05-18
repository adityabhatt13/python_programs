# str = input().split()
# n,m = int(str[0]),int(str[1])
# b = input().split()
# li = [[b[m*i+j]for j in range(m)]for i in range(n)]
# print(li)


str = input().split()
n,m = int(str[0]),int(str[1])
b = str[2:]
li = [[b[m*i+j]for j in range(m)]for i in range(n)]
print(li)


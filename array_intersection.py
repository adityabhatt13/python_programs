n = int(input())
li1 = [int(x) for x in input().split()]
m = int(input())
li2 = [int(x) for x in input().split()]

common = []
for i in range(0,n):
    for j in range(0,m):
        if li1[i] == li2[j]:
            common.append(li1[i])
            break
print(common)

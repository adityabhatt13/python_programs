n = int(input())
li = [int(x) for x in input().split()]
for i in range(0,n):
    flag = False
    for j in range(0,i):
        if li[i] == li[j]:
            flag = True
            break
    else:
        print(li[i])

                   
            
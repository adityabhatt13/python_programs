n = int(input())
for k in range(2, n+1):
    for d in range(2, k):
        if k%d == 0:
            break
    else:
        print(k)                
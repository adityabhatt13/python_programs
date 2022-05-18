n = int(input())
for i in range(1,n+1):
    for j in range(1,2*n+2):
        if i==j:
            print('*', end = "") 
        elif j == n + 1 or j == 2*n+2 - i:
            print('*', end = "")
        else:
            print(0, end = "")
    print()

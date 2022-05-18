n = int(input())
for i in range(1, (n+1)//2 + 1): #from row 1 to 3
    for space in range((n+1)//2 - i):
        print(" ", end = "")
    for j in range((i*2)-1):
        print("*", end = "")
    print()

for i in range((n+1)//2 + 1, n + 1): #from row 4 to 5
    for space in range(i - (n+1)//2):
        print(" ", end = "")
    for j in range((n+1 - i)*2 - 1):
        print("*", end = "")
    print()
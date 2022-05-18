n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    space = i*2
    while space < n*2:
        print(" ", end="")
        space += 1
    j = i   
    while j >= 1:
        print(j, end="")
        j -= 1   
    print()
    i += 1
    
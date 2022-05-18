while True:
    n =int(input())
    if n >= 1 and n <= 5:
        a = int(input())
        b = int(input())
        if n == 1:
            print(a+b)
        elif n == 2:
            print(a-b)
        elif n == 3:
            print(a*b)
        elif n == 4:
            print(a//b)
        else:
            print(a%b)
    elif n == 6:
        break
    else:
        print("Invalid Operation")
                                        
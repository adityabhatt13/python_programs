def checkArmstrong(n):
    a = n
    digits = 0
    while a > 0:
        digits += 1
        a = a // 10

    arm_number = 0
    for c in str(n):
        c = int(c)
        c = c**digits
        arm_number = arm_number + c
    if n == arm_number :
        return True 
    else:
        return False

n = int(input())
armstrong = checkArmstrong(n)
if armstrong:
    print("true")
else:
    print("false")                    




    
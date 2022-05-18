def check_palindrome(n):
    actual_num = n
    rev = 0
    while n > 0:
        remainder = n % 10
        rev = rev*10 + remainder
        n = n // 10
        if (actual_num==rev or rev == 0):
            return True
    else:
        return False        

n = int(input())
if check_palindrome(n):
    print("true")
else:
    print("false")    
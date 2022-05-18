actual_num = int(input())
num = actual_num
rev = 0
while num > 0:
    remainder = num % 10
    rev = rev*10 + remainder
    num = num//10
if rev == actual_num:
    print("palindrome")
else:
    print("not palindrome")        


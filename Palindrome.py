num = int(input())
actual_num = num
rev = 0
while num > 0:
    remainder = num % 10
    rev = rev*10 + remainder
    num = num // 10
if (actual_num==rev):
    print("True")
else:
    print("False")        

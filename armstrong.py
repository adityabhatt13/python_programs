n = int(input())
pow = len(str(n))
sum = 0
temp = n
while temp > 0:
    remainder = temp%10
    sum = sum + remainder**pow
    temp = temp//10
if n == sum:
    print("true")
else:
    print("false")        

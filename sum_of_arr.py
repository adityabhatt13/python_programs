arr1 = [6,2,4]
arr2 = [3,4]
if len(arr1) >= len(arr2):
    zeroes = len(arr1) - len(arr2)
    for i in range(zeroes):
        arr2.insert(0,0)
else:
    zeroes = len(arr2) - len(arr1)
    for i in range(zeroes):
        arr1.insert(0,0)

s = []
n = max(len(arr1),len(arr2))
carry = 0
for i in range(n-1,-1,-1):
    sum1 = arr1[i] + arr2[i] + carry
    if sum1 > 9 and i != 0:
        sum1 = sum1%10
        carry = 1
    else:
        carry = 0      
    s.append(str(sum1))
s = s[::-1]
s = "".join(s)
s = [x for x in s]
s = " ".join(s)
print(s)     
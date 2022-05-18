a = [6,9,8,5]
b = []
n = len(a)
m = len(b)
sum = [0] * n
i = n - 1
j = m - 1
k = n - 1
carry = 0
s = 0 
while j >= 0:
    s = a[i] + b[j] + carry
    sum[k] = (s % 10)
    carry = s // 10  
    k-=1
    i-=1
    j-=1
while i >= 0:
    s = a[i] + carry
    sum[k] = (s % 10)
    carry = s // 10     
    i-=1
    k-=1
# ans = 0
# if carry:
#     ans = 10
# for i in range(n):
#     ans += sum[i]
#     ans *= 10
# ans = ans//10
# ans = [x for x in str(ans)]
# print(ans)
print(sum)
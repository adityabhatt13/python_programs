n = int(input())
i = 2
found = False
while i < n:
    if n%i == 0:
        found = True
    i += 1

if found:
    print("Not Prime")
else:
    print("Prime")    

# n = int(input())
# k = 2
# while k <= n:
#     i = 2
#     found = False
#     while i < k:
#         if k%i == 0:
#             found = True
#         i += 1
#     if not(found):
#         print(k)
#     k += 1    
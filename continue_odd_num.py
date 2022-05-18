# for i in range(1, 101):
#     if i%2 == 0:
#         continue
#     print(i)


n = int(input())
for i in range(2, n+1, 2):
    if i%7 == 0:
        continue
    print(i)


# i=1
# while i<3:
#     j=0
#     while j<5:
#         j = j + 1
#         if j==3:
#             continue
#         print(j,end="")
#     i = i + 1

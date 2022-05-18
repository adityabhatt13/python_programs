# #line separated input
# n = int(input())
# li = []
# for i in range(n):
#     li.append(int(input()))
# print(li)    

# #space separated input
# str = input()
# str_split = str.split()
# for i in str_split:
#     li.append(int(i))

n = int(input())

li = [int(x) for x in input().split()]
for ele in li:
    print(ele)

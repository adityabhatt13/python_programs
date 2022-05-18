def reverse(li):
    length = len(li)
    for i in range(length//2):
        li[i], li[-i-1] = li[-i-1], li[i]

li = [1,2,3,4,5,6]
reverse(li)
print(li)

li = li[::-1]
print(li)
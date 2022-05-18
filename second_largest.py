# arr = [1,5,0,9,10,45,2,3,5]
# highest = max(arr)
# arr.remove(highest)
# print(max(arr))

li = [1,3,41,5,12]

max = max(li[0],li[1])
secondmax = min(li[0],li[1])
# print(max)
# print(secondmax)
n = len(li)
for i in range(2,n):
    if li[i]>max:
        secondmax = max
        max = li[i]
    elif li[i]>secondmax and max != li[i]:
        secondmax = li[i]
else:        
    print(secondmax)           
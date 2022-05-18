arr = [1,2,3,4,5,6,7]
rotation = 2
temp = []
i = 0
while i < rotation:
    temp.append(arr[i])
    i += 1
i = 0
while rotation < len(arr):
    arr[i] = arr[rotation]
    i += 1
    rotation += 1
arr[:] = arr[:i] + temp
print(arr)    
arr = [int(x) for x in input().split()]
for i in range(len(arr)):
    if arr[i] == 0:
        arr.append(arr[i])
        arr.remove(arr[i])
    else:
        continue

k = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[k] = arr[i]
        k+=1
for j in range(k,len(arr)):
    arr[j] = 0

print(arr)    
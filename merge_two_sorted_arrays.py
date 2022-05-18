arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
arr3 = []
i,j = 0,0
len1,len2 = len(arr1),len(arr2)

while i < len1 and j < len2:
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1

while i < len1:
    arr3.append(arr1[i])
    i += 1

while j < len2:
    arr3.append(arr2[j])
    j += 1
print(arr3)    



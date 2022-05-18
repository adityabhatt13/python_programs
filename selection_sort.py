arr = [20,12,10,15,2]
for step in range(len(arr)):
    min = step
    for i in range(step+1,len(arr)):
        if arr[i] > arr[min]:
            min = i
    arr[step],arr[min] = arr[min],arr[step]        
print(arr)            
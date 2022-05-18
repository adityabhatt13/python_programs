arr = [10,20,30,1]
n = len(arr)
minimum = arr[0]
min_index = 0
for i in range(n):
    if minimum > arr[i]:
        minimum = arr[i]
        min_index = i
print(min_index)        


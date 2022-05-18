def liner_search(li, to_search):
    for i in range(len(li)):
        if li[i] == to_search:
            return i
    return -1

li = [1, 2, 3, 4, 6, 5]
index = liner_search(li,10)
print(index)

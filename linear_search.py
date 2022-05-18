n = int(input())
li = [int(x) for x in input().split()]
to_search = int(input())
for x in li:
    if x == to_search:
        print("Found at index", li.index(x))
        break
else:
    print("Not Found")        

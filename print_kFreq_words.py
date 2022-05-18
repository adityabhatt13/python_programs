s = input()
k = int(input())
words = s.split()
# d = {}
# for w in words:
#     if w in d:
#         d[w] = d[w] + 1
#     else:
#         d[w] = 1
# print(d)
d = {}
for w in words:
    d[w] = d.get(w,0) + 1
for w in d:
    if d[w] == k:
        print(w)
    else:
        print("no word comes",k,"times")
        break    
           
li = [1,2,3,4,51,1,6,3,9,0,3,2,1,7,4,2,1,9,0,7,4,1,4,5,32,6]
di = {}
for i in li:
    if i not in di:
        di[i] = 1
    else:
        di[i] += 1
max_freq = 0
for i in di.keys():
    max_freq = max(di[i],max_freq)
max_ele = di.get(max_freq)  
print(max_ele,":",max_freq)   

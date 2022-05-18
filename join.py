a = "abc".join(["1","2","3"])
print(a)

li = [[1,2,3,4],[5,6],[9,10,11]]
n = 3
for row in li:
    output = ' '.join([str(ele) for ele in row])
    print(output)        
